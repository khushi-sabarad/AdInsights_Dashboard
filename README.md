# AdInsights Dashboard

This project is a web-based dashboard that provides interactive visualizations and analysis of digital advertising performance data. It uses a dataset of 10,000 rows, containing ad campaign metrics to display key insights into click-through rates (CTR), conversion rates, and other relevant metrics. Users can filter the data by gender, ad type, and location to explore specific segments of the audience.

## Features

* **Interactive Visualizations:** Uses Plotly to create dynamic charts and graphs.
* **Data Filtering:** Allows users to filter data by gender, ad type, and location.
* **Outlier Handling:** Implements basic outlier removal for age and income data.
* **Key Performance Metrics:** Displays key ad performance metrics (CTR, conversion rate, etc.).

## Technologies Used

* Python
* Pandas
* Plotly
* Flask
* HTML/CSS

## Setup

1.  Clone the repository:

    ```bash
    git clone [repository_url]
    ```

2.  Navigate to the project directory:

    ```bash
    cd ad_dashboard
    ```

3.  Install the required libraries:

    ```bash
    pip install -r requirements.txt
    ```

4.  Download the dataset:

    * The dataset, "Dataset: Online Advertisement Click-Through Rates", is available from Mendeley Data.
    * Download it from: [doi: 10.17632/wrvjmdtjd9.1](doi: 10.17632/wrvjmdtjd9.1)
    * Place the downloaded `Dataset_Ads.csv` file in the project's root directory.

5.  Run the application:

    ```bash
    python app.py
    ```

6.  Open your browser and go to `http://127.0.0.1:5000/`.

## Dataset

This project uses the "Dataset: Online Advertisement Click-Through Rates" dataset, containing 10,000 rows.

**Citation:**

[Tawade, Jagadish; Kulkarni, Nitiraj (2024), “Dataset: Online Advertisement Click-Through Rates”, Mendeley Data, V1, doi: 10.17632/wrvjmdtjd9.1](Tawade, Jagadish; Kulkarni, Nitiraj (2024), “Dataset: Online Advertisement Click-Through Rates”, Mendeley Data, V1, doi: 10.17632/wrvjmdtjd9.1)

## Future Enhancements

* Implement more advanced filtering options.
* Add predictive analytics features.
* Deploy the application to a cloud platform (e.g., Google Cloud Platform).
* Add more metrics and visualizations.
