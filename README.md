# 📊 Data Pipeline Project – Glue + Airflow + Iceberg

## Objectif
Ingestion de transactions.csv et tiers.csv, transformation PySpark, orchestration Airflow MWAA, sauvegarde en Apache Iceberg dans S3.

## 📁 Arborescence
```
project-data-pipeline/
├── dags/
│   └── main_dag.py
├── glue_jobs/
│   ├── job_ingest.py
│   └── job_transform.py
├── terraform/
│   └── main.tf
├── README.md
```

## 🔧 Étapes locales
1. Cloner le projet :
```bash
git clone https://github.com/ton-user/project-data-pipeline.git
cd project-data-pipeline
```

2. Écrire les fichiers `transactions.csv` et `tiers.csv` dans S3 bucket : `s3://your-bucket/raw/`

3. Modifier les chemins dans les scripts Glue (`glue_jobs/*.py`)

4. Déployer les ressources AWS avec Terraform :
```bash
cd terraform
terraform init
terraform apply
```

5. Déployer les scripts PySpark dans S3 :
```bash
aws s3 cp ../glue_jobs/job_ingest.py s3://your-bucket/scripts/
aws s3 cp ../glue_jobs/job_transform.py s3://your-bucket/scripts/
```

6. Déployer le DAG sur MWAA (Airflow managé AWS) :
```bash
aws s3 cp ../dags/main_dag.py s3://your-airflow-dag-bucket/dags/
```

7. Vérifier dans MWAA et exécuter le DAG.

## ✅ Résultat attendu
- Fichier Iceberg : `s3://your-bucket/gold/transactions_iceberg/`
- Suivi orchestration dans Airflow (MWAA)