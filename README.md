# UberData-DataEngineering
## Introduction
The primary goal of this project is to build a complete data engineering pipeline using Google Cloud Platform (GCP) and Mage.ai. The pipeline will extract Uber trip data from Google Cloud Storage (GCS), perform data cleaning and transformation operations within Mage.ai, and load the processed data back into GCS. Once the data is clean and ready, we will leverage BigQuery for analytical queries and data exploration. Finally, the project will conclude with creating visualizations using Looker to derive insights from the data.

<br> This end-to-end project aims to showcase a real-world data engineering workflow, demonstrating data ingestion, transformation, storage, querying, and visualization using modern cloud-based tools.

## Dataset
The dataset used in the project has been uploaded in the repository. But, to get more information about the source of the data, you can visit this website: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page

---

## Google Cloud Platform (GCP) Setup

### 1. Enable Billing
- Ensure your Google Cloud project has billing enabled to access required GCP services.
- Link your billing account under the **Billing** section of the GCP Console.

### 2. Enable APIs
- Navigate to **APIs & Services** in the GCP Console.
- Enable the following APIs if not already enabled:
  - **Google Cloud Storage API**
  - **BigQuery API**
  - **Looker API** (if needed later for Looker integration)

### 3. Create a Cloud Storage Bucket
- Go to **Cloud Storage > Buckets** and click **Create**.
- Configure the following:
  - **Bucket name:** Choose a globally unique name.
  - **Location:** Select multi-region or region based on your requirement.
  - **Storage Class:** Choose based on data usage:
    - **Standard:** Frequently accessed data
    - **Nearline/Coldline:** For infrequently accessed data
  - **Access Control:** Decide between Uniform or Fine-grained access.
- Create the bucket once the settings are finalized.

### 4. Upload Data to Cloud Storage
- Navigate to **Cloud Storage > Browser** and select your bucket.
- Click **Upload Files** or **Upload Folder** to upload the dataset from your local system.
- Verify that the data is successfully uploaded.

## Mage.ai Pipeline - Extract, Transform, Load (ETL)
### 1. Connect Mage.ai to GCP
- Configure Mage.ai to access your Google Cloud Storage bucket using service account credentials.
- Use Mage's GCS connector to fetch the uploaded dataset.

### 2. Data Extraction
- Extract the raw dataset from GCS using Mage.ai’s extraction blocks.
- Read the data into Mage’s pipeline for preprocessing.

### 3. Data Transformation
- Perform data cleaning tasks such as:
  - Handling missing values
  - Removing duplicates
  - Converting data types
  - Filtering outliers
- Perform feature engineering if necessary (e.g., calculating trip duration or fare per mile).
- Validate and test the transformations.

### 4. Load Transformed Data
- Store the clean and transformed dataset back into a **new GCS bucket** or a **designated folder** in the same bucket.
- Save the data in formats like CSV, Parquet, or Avro based on downstream requirements.

---

## BigQuery - Analytics Layer

### 1. Load Data into BigQuery
- Create a **dataset** and **table** in BigQuery.
- Load the transformed dataset from GCS into the BigQuery table.
- Set schema either manually or let BigQuery auto-detect.

### 2. Perform SQL Analytics
- Write SQL queries to analyze the trip data, examples:
  - Average trip distance per month
  - Most frequent pickup locations
  - Peak hours for rides
  - Revenue generated per day/month
- Perform aggregations, joins, and window functions as needed.

---
