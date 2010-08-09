all:

install: condor-ec2-node.init
	install -D -m0755 condor-ec2-node.init $(DESTDIR)/etc/init.d/condor-ec2-node
