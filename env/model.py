import paddle
import paddle.nn as nn
import paddle.nn.functional as F
class MultiTaskLSTM(paddle.nn.Layer):
    """多任务LSTM时序预测模型
    LSTM为共享层网络，对两个预测目标分别有两个分支独立线性层网络
    
    TODO 其实该模型就是个Encoder，如果后续要引入天气预测未来的变量，补充个Decoder，
    然后Encoder负责历史变量的编码，Decoder负责将 编码后的历史编码结果 和 它编码未来变量的编码结果 合并后，做解码预测即可
    """
    def __init__(self,input_len=120*4, pred_len=24*4):
        super(MultiTaskLSTM, self).__init__()
        self.Conv1D1=paddle.nn.Conv1D(480,256,2,padding='same') 
        # self.batch_norm  = paddle.nn.BatchNorm1D(256)   
        self.lstm_layer = paddle.nn.LSTM(14, 10, 
                                    num_layers=1, 
                                    direction='forward')
        self.bilstm_layer = paddle.nn.LSTM(10, 32, 
                                    num_layers=1, 
                                    direction='bidirect')
        self.relu=paddle.nn.ReLU()
        self.multihead_attention = paddle.nn.MultiHeadAttention(embed_dim=256, num_heads=4)
                    
        # 为'ROUND(A.POWER,0)'构建分支网络
        self.linear1_1 = paddle.nn.Linear(in_features=16384, out_features=100)
        self.linear1_2 = paddle.nn.Linear(in_features=100, out_features=96)
        # 为'YD15'构建分支网络 
        self.linear2_1 = paddle.nn.Linear(in_features=16384, out_features=100)
        self.linear2_2 = paddle.nn.Linear(in_features=100, out_features=96)


        
    def forward(self, x):
        output=self.Conv1D1(x)
        # output=self.batch_norm(output)
        output=self.relu(output)
        output, (hidden, cell) = self.lstm_layer(output)
        output=self.relu(output)
        output, (hidden, cell) = self.bilstm_layer(output)
        output=self.relu(output)
        # 使用循环注意力机制
        output = paddle.transpose(output, perm=[0, 2, 1])  # 将序列长度置于第三维度
        output= self.multihead_attention(output)
        output = paddle.transpose(output, perm=[0, 2, 1])  # 恢复原来的维度顺序

        output = paddle.reshape(output, [len(output), -1])

        output1 = self.linear1_1(output)
        output1=self.relu(output1)
        output1 = self.linear1_2(output1)

        output2 = self.linear2_1(output)
        output2=self.relu(output2)
        output2 = self.linear2_2(output2)
        return [output1, output2]
class MultiTaskMSELoss(paddle.nn.Layer):
    """
    设置损失函数, 多任务模型，两个任务MSE的均值做loss输出
    """
    def __init__(self, weight1=0.0, weight2=1.0):
        super(MultiTaskMSELoss, self).__init__()
        self.weight1 = weight1
        self.weight2 = weight2

    def forward(self, inputs, labels):
        mse_loss = paddle.nn.loss.MSELoss()
        mse1 = mse_loss(inputs[0], labels[:,:,0].squeeze(-1)) * self.weight1
        mse2 = mse_loss(inputs[1], labels[:,:,1].squeeze(-1)) * self.weight2
        # TODO 也可以自行设置各任务的权重，让其更偏好YD15
        # 即让多任务有主次之分
        return mse1, mse2, (mse1 + mse2) / 2