all:
dist: condor-ec2-node.tar.gz

install: condor-ec2-node.init
	install -D -m0755 condor-ec2-node.init $(DESTDIR)/etc/rc.d/init.d/condor-ec2-node

condor-ec2-node.tar.gz: condor-ec2-node.init Makefile README LICENSE-2.0.txt
	mkdir condor-ec2-node
	cp $^ condor-ec2-node
	tar czfv $@ condor-ec2-node
	rm -rf condor-ec2-node
