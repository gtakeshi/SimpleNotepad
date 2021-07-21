from twisted.internet import reactor
from twisted.internet.protocol import Protocol,Factory

class SimpleLogger(Protocol):

    def connectionMade(self):
        print("Got connection from",self.transport.client)

    def connectionLost(self,reason):
        print(self.transport.client,"Disconnect")

    def dataReceived(self, data):
        print(str(data))

factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(1234,factory)
reactor.run()