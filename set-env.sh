unset BLDGNAME
unset BLDGNUM
unset ROOMNUM
unset EndpointID
unset ROOMCAP
unset IPADDRESS

echo "Enter Building Name: " 

read BLDGNAME

echo "Enter Building Number: " 

read BLDGNUM

echo "Enter Room Number: " 

read ROOMNUM

echo "Enter EndpointID: " 

read ENDPTID

echo "Enter Maximum Capacity: " 

read ROOMCAP

echo "export BLDGNAME=$BLDGNAME" >> ~/.bashrc
echo "export BLDGNUM=$BLDGNUM" >> ~/.bashrc
echo "export ROOMNUM=$ROOMNUM" >> ~/.bashrc
echo "export ENDPTID=$ENDPTID" >> ~/.bashrc
echo "export ROOMCAP=$ROOMCAP" >> ~/.bashrc
echo "export IPADDRESS=cscap1.iot.nau.edu" >> ~/.bashrc


. ~/.bashrc
