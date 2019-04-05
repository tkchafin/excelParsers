#!/bin/bash

#grab fresh master file from progress_overview
echo "Getting fresh master database..."
python3 ./xlsxWTDprogress2masterlist.py /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_progress-overview_mrd_190305.xlsx

echo ""
echo "Trying to find coordinates..."
#try to get some coordinates filled in
echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/OLD/WTD_master_database.xlsx"
python3 ./xlsxWTDupdatemasterCoords.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/OLD/WTD_master_database.xlsx field

echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/phase3_batch3_2-5-19_all.xlsx"
python3 ./xlsxWTDupdatemasterCoords.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/phase3_batch3_2-5-19_all.xlsx field

echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/WTD_fieldDate_phase3.1_2018.xlsx"
python3 ./xlsxWTDupdatemasterCoords.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/WTD_fieldDate_phase3.1_2018.xlsx field

echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/CWD_phase3.2_batch2_samples_field-data.xlsx"
python3 ./xlsxWTDupdatemasterCoords.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/CWD_phase3.2_batch2_samples_field-data.xlsx field

echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/CWD_phase3.2_samples_field-data_bak.xlsx"
python3 ./xlsxWTDupdatemasterCoords.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/CWD_phase3.2_samples_field-data_bak.xlsx field

echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_progress-overview_btm_missingCWD-table_190326.xlsx"
python3 ./xlsxWTDupdatemasterCoords.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_progress-overview_btm_missingCWD-table_190326.xlsx dna

echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/phase3.2_CHOSEN_SAMPLES_tkc.xls"
python3 ./xlsxWTDupdatemasterCoords.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/phase3.2_CHOSEN_SAMPLES_tkc.xls field

echo""

echo "Trying to fill in age/sex information..."
echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/OLD/WTD_master_database.xlsx"
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/OLD/WTD_master_database.xlsx field age
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/OLD/WTD_master_database.xlsx field sex

echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/phase3_batch3_2-5-19_all.xlsx"
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/phase3_batch3_2-5-19_all.xlsx field age
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/phase3_batch3_2-5-19_all.xlsx field sex

echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/WTD_fieldDate_phase3.1_2018.xlsx"
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/WTD_fieldDate_phase3.1_2018.xlsx field age
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/WTD_fieldDate_phase3.1_2018.xlsx field sex

echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/CWD_phase3.2_batch2_samples_field-data.xlsx"
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/CWD_phase3.2_batch2_samples_field-data.xlsx field age
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/CWD_phase3.2_batch2_samples_field-data.xlsx field sex

echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/CWD_phase3.2_samples_field-data_bak.xlsx"
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/CWD_phase3.2_samples_field-data_bak.xlsx field age
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/CWD_phase3.2_samples_field-data_bak.xlsx field sex

echo "Checking /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/phase3.2_CHOSEN_SAMPLES_tkc.xls"
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/phase3.2_CHOSEN_SAMPLES_tkc.xls field age
python3 ./xlsxWTDupdatemasterAgeSex.py wtd_master.xlsx /Volumes/acamel_server/aCaMEL-Projects/4_Mammals/WTD/WTD_field_data/phase3.2_CHOSEN_SAMPLES_tkc.xls field sex



