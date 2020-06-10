import socket
class interface:
    REMOTE_SERVER = "one.one.one.one"
    def is_connected(hostname):
      try:
        # see if we can resolve the host name -- tells us if there is
        # a DNS listening
        host = socket.gethostbyname(hostname)
        # connect to the host -- tells us if the host is actually
        # reachable
        s = socket.create_connection((host, 80), 2)
        s.close()
        return True
      except:
         print("İnternet baglantınız bulunmamaktadır. Lütfen internet baglantınızı kontrol edin.")
      return False
