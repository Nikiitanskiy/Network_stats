from speedtest import Speedtest

class SpeedTesting:
    def __init__(self):
        pass
    def start_test(self):
        result = {}
        try:
            st = Speedtest()
            threads = 1
            download = st.download(threads=threads)
            upload = st.upload(threads=threads)
            result = \
                {
                    "Download" : round(download/(2**20)),
                    "Upload" : round(upload/(2**20))
                }
            
            return result
        except Exception as e:
            return  "Testing is not available right now. Error:" + str(e)

# st = SpeedTesting()
# print(st.start_test()[0])

