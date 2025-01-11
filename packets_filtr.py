import psutil


class Tools:
    def __init__(self):
        pass

    def get_netstats(self):
        dict_net_adap = psutil.net_io_counters(pernic=True)
        return dict_net_adap
    
    def traffic_stats(self):
        try:
            list_of_adap = self.get_netstats()
            list_of_names = list_of_adap.keys()
            list_of_val_adap = psutil.net_if_addrs()
            result = []
            for adap in list_of_names:
                result.append({
                    "Name" : adap,
                    "MBytes sent" : round(list_of_adap[adap][0]/(2**20)),
                    "MBytes received" : round(list_of_adap[adap][1]/(2**20)),
                    "Packets sent" : list_of_adap[adap][2],
                    "Packets received" : list_of_adap[adap][3],
                    "MAC" : list_of_val_adap[adap][0][1],
                    "IP" : list_of_val_adap[adap][1][1]
                    
                })
                    
            return result 
        except Exception as e:
            return e


# Nt = Tools()
# dict = Nt.traffic_stats()

# ps  = psutil.net_if_addrs()
# # print(ps['Ethernet 2'])
# # print(Nt.traffic_stats())
# print(dict)
# for i in dict:
#     print(i)

#     print('\n\n\n')
