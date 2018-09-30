# 写一个类，其功能是：1.解析指定的歌词文件的内容 2.按时间显示歌词
# 提示：歌词文件的内容一般是按下面的格式进行存储的。
# 歌词前面对应的是时间，在对应的时间点可以显示对应的歌词
class Lyric:
    def __init__(self,time,word):
        self.time = time
        self.word = word
    def __str__(self):
        return "%.2f %s" % (self.time,self.word)
    def __gt__(self, other):
        return self.time >other.time



class LyricAnalysis:
    """歌词解析类"""
    def __init__(self,song_name):
        #一个歌词解析器对象对应一首歌
        self.song_name = song_name
        #一首歌对应一个容器
        self.all_lyric = []

        #解析歌词
        self.collect_lyric()


    def get_time_word(self,content):
        contents = content.split("]")
        word = contents[-1]
        for time in contents[:-1]:
            times = time[1:].split(":")
            fen = float(times[0])
            miao = float(times[1])
            new_time = fen*60 + miao
            # print(new_time,word)
            #根据时间和词创建歌词对象
            lyric = Lyric(new_time,word)
            self.all_lyric.append(lyric)



    def collect_lyric(self):
        """将时间和词提取出来"""
        try:

            with open("./files/%s.txt" % self.song_name,"r",encoding="utf-8") as f:
                line = f.readline()
                while line:
                    #将每一行的内容和词显示出来
                    self.get_time_word(line)
                    line = f.readline()

                #排序
                self.all_lyric.sort(reverse=True)
                # for lyric in self.all_lyric:
                #     print(lyric)

        except:
            print("文件不存在")

    def get_word(self,time):
        for lyric in self.all_lyric:
            if lyric.time <= time:
                return lyric.word

song1 = LyricAnalysis("蓝莲花")
song1.collect_lyric()
print(song1.get_word(20))

