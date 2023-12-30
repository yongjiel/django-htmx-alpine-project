#!/bin/bash
set -e


echo "---Go to work dir back_end......"
cd back_end
echo "---Now in directory back_end."

echo "---Run backend to start srever and load data...."
./config_start_backend_server_load_data.sh
echo "---Backend Done."

echo "---Go to work dir front_end......"
cd ../front_end
echo "---Now in directory front_end."

echo "---Run frontend to start srever...."
./config_start_frontend_server.sh
echo "---Frontend Done."

