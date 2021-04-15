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

read ENDPOINTID

echo "Enter Maximum Capacity: " 

read ROOMCAP

echo "export BLDGNAME=$BLDGNAME" >> ~/.bashrc
echo "export BLDGNUM=$BLDGNUM" >> ~/.bashrc
echo "export ROOMNUM=$ROOMNUM" >> ~/.bashrc
echo "export ENDPOINTID=$ENDPOINTID" >> ~/.bashrc
echo "export ROOMCAP=$ROOMCAP" >> ~/.bashrc
echo "export IPADDRESS=172.20.64.38:5000" >> ~/.bashrc


. ~/.bashrc