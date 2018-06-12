#-*-coding:utf-8 -*-
__author__ = 'dell'

# from numpy import *
# import operator
# import pickle
# import matplotlib.pylab as plt

# def knn(data, trainData, laber,k):
#     # trainData = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
#     # laber = ['A', 'A', 'B', 'B']
#     # data = [1.0, 1.1]
#     trainDataSize = trainData.shape[0]
#     distance = tile(data, (trainDataSize, 1)) - trainData
#     Distance = distance**2
#     EuclideanDistance = Distance.sum(axis=1)**0.5
#     sortedDistIndicies = EuclideanDistance.argsort()
#     classCount = {}
#
#     for i in range(k):
#         voteIlabel = laber[sortedDistIndicies[i]]
#         classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
#     sortedClass = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
#     return sortedClass[0][0]
#
# def file2array(filename):
#     with open(filename) as file:
#         datalines = file.readlines()
#     laber = []
#     returnDatas = zeros((len(datalines),3))
#     index = 0
#     for dataline in datalines:
#         dataline = dataline.strip()
#         datas = dataline.split("\t")
#         # datas = re.split(r"\s*\t\s*", dataline) # 用正则表达式进行分割
#
#         laber.append(int(datas[-1]))
#         returnDatas[index,:] = datas[0:3]
#         index = index + 1
#     pickle.dump(returnDatas, file("returnDatas.pkl", "wb"), -1)
#     pickle.dump(laber, file("laber.pkl", "wb"), -1)
#     return returnDatas, laber
#
# def plot():
#     returnDatas = pickle.load(file("returnDatas.pkl", "rb"))
#     laber = pickle.load(file("laber.pkl", "rb"))
#     fig = plt.figure()
#     ax = fig.add_subplot(111)
#     ax.scatter(returnDatas[:, 1], returnDatas[:, 2], 15.0 * array(laber), 15.0 * array(laber))
#     ax.axis([-2, 25, -0.2, 2.0])
#     plt.xlabel('Percentage of Time Spent Playing Video Games')
#     plt.ylabel('Liters of Ice Cream Consumed Per Week')
#     plt.show()
# def autoNorm(dataSet):
#     minVals = dataSet.min(0)
#     maxVals = dataSet.max(0)
#     range = maxVals - minVals
#
#     waitNorm = dataSet - tile(minVals,(dataSet.shape[0], 1))
#     normData = waitNorm/tile(range, (dataSet.shape[0], 1))
#
#     return normData
# def datingClassTest():
#     returnData = pickle.load(file("returnDatas.pkl", "rb"))
#     laber = pickle.load(file("laber.pkl", "rb"))
#     returnData = autoNorm(returnData)
#     ratio = 0.1
#     length = returnDatas.shape[0]
#     errorCount = 0.0
#     for i in range(int(ratio*length)):
#         result = knn(returnData[i], returnData[int(ratio*length):length,:], laber[int(ratio*length):length], 3)
#         print "result = {0}, rawDataClass = {1}".format(result, laber[i])
#         if result != laber[i]:
#             errorCount = errorCount + 1.0
#
#     print "error rate is {0}".format(errorCount/float(int(ratio*length)))


if __name__ == '__main__':
    import pickle, kNN
    returnDatas = pickle.load(file("returnDatas.pkl", "rb"))
    # print knn(a, group, labels, 3)
    # returnDatas, laber = file2array("datingTestSet2.txt")
    # plot()
    # autoNorm(returnDatas)
    # datingClassTest()
    from PIL import Image
    image = Image.open(u"F:/验证码/字符验证/download/0.jpg")
    imgry = image.convert('L')
    # table = get_bin_table()
    # out = imgry.point(table, '1')
    # image.show()
    imgry.show()


