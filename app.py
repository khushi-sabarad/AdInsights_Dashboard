import pandas as pd
from flask import Flask, render_template, request
import plotly.express as px
from datetime import datetime

app = Flask(__name__)

# Load the dataset
df = pd.read_csv("Dataset_Ads.csv")
df['Click Time'] = pd.to_datetime(df['Click Time'])
df.dropna(inplace=True)
df['Day of Week'] = df['Click Time'].dt.day_name()

def generate_plots(data):
    # Example plots (you can add more)
    ctr_by_ad_type = data.groupby('Ad Type')['CTR'].mean().reset_index()
    fig_ctr_ad_type = px.bar(ctr_by_ad_type, x='Ad Type', y='CTR', title='Average CTR by Ad Type')
    ctr_ad_type_html = fig_ctr_ad_type.to_html(full_html=False)

    fig_age_clicks = px.scatter(data, x='Age', y='Clicks', title='Age vs. Clicks')
    age_clicks_html = fig_age_clicks.to_html(full_html=False)

    fig_income_hist = px.histogram(data, x='Income', title='Income Distribution')
    income_hist_html = fig_income_hist.to_html(full_html=False)

    clicks_over_time = data.groupby(data['Click Time'].dt.date)['Clicks'].sum().reset_index()
    fig_clicks_time = px.line(clicks_over_time, x="Click Time", y="Clicks", title="Clicks over time")
    clicks_time_html = fig_clicks_time.to_html(full_html=False)

    conversion_by_location = data.groupby('Location')['Conversion Rate'].mean().reset_index()
    fig_conversion_location = px.bar(conversion_by_location, x='Location', y='Conversion Rate', title="Average conversion rate by location")
    conversion_location_html = fig_conversion_location.to_html(full_html=False)

    ctr_by_gender = data.groupby('Gender')['CTR'].mean().reset_index()
    fig_ctr_gender = px.bar(ctr_by_gender, x='Gender', y='CTR', title="Average CTR by Gender")
    ctr_gender_html = fig_ctr_gender.to_html(full_html=False)

    return {
        'ctr_ad_type': ctr_ad_type_html,
        'age_clicks': age_clicks_html,
        'income_hist': income_hist_html,
        'clicks_time': clicks_time_html,
        'conversion_location': conversion_location_html,
        'ctr_gender': ctr_gender_html,
    }

@app.route('/', methods=['GET', 'POST'])
def index():
    filtered_df = df.copy()  # Start with a copy of the original data

    if request.method == 'POST':
        gender_filter = request.form.get('gender')
        ad_type_filter = request.form.get('ad_type')
        location_filter = request.form.get('location')

        if gender_filter and gender_filter != 'All':
            filtered_df = filtered_df[filtered_df['Gender'] == gender_filter]
        if ad_type_filter and ad_type_filter != 'All':
            filtered_df = filtered_df[filtered_df['Ad Type'] == ad_type_filter]
        if location_filter and location_filter != 'All':
            filtered_df = filtered_df[filtered_df['Location'] == location_filter]

    plots = generate_plots(filtered_df)

    #Create the filter options
    genders = ['All'] + sorted(df['Gender'].unique().tolist())
    ad_types = ['All'] + sorted(df['Ad Type'].unique().tolist())
    locations = ['All'] + sorted(df['Location'].unique().tolist())

    return render_template('index.html', **plots, genders = genders, ad_types = ad_types, locations = locations)

if __name__ == '__main__':
    app.run(debug=True)