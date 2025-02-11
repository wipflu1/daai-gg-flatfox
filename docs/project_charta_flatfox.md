# `Project Outline for Predicting Flat Prices` - Project Charta
## Problem Definition
The housing brokerage market in Switzerland is highly competitive. Flatfox AG aims to maintain its competitive edge by enhancing its product offerings. 
Currently, Flatfox.ch does not have a feature to check the prices of housing listings, leaving users without the tools to estimate fair flat prices. 
Although the platform is popular for listing flats, the lack of this feature poses a significant challenge.

## Situation Assessment
Several of Flatfox's competitors already offer tools for checking flat prices, providing their users with valuable insights and enhancing their overall experience. 
By developing a similar tool, Flatfox.ch has a significant opportunity to improve user experience and build greater trust among its users. 
This strategic enhancement will not only position Flatfox.ch as a more reliable and user-friendly option but also help differentiate it from competitors, attracting more users to the platform and strengthening its market position.

## Project Goals and Success Criteria
The goal of this project is to develop a predictive model to estimate the price of flats listed on Flatfox.ch based on parameters like the number of rooms, location, and living space.
This will help users make informed decisions and avoid overpaying for their desired properties.
We aim to provide customers with accurate price estimates for flats based on their desired features. 
This tool will help customers avoid overpaying during their apartment search, ensuring they make informed decisions and get fair deals on their chosen properties.
Our project will enhance the customers decision process by providing price comparisons, giving customers the confidence that they are making the best possible choice within their budget.

Our project can also be repurposed to benefit flat owners, ensuring they receive the right amount of money from their investments. 
By utilizing our accurate price estimation tool, owners can gauge the true market value of their properties based on location, size, amenities, and current market trends. 
This data-driven approach allows them to set competitive and fair prices, attract potential buyers or renters, and maximize their returns. Additionally, the platform can offer insights into market fluctuations and optimal listing times, helping owners make informed decisions to enhance their investment outcomes.

## Data Mining Goals
Here we define the milestones for the Project. 
- Data Collection Complete
- Data Cleaning and Preprocessing Completed
- Feature Engineering Complete
- Initial Model Development and Training
- Model Evaluation and Refinement
- Deployment
- Final Documentation and Project Report

### Key Metrics

The model's performance will be evaluated using the following key metrics:

1. **Prediction Accuracy:** 
   - The model should predict flat prices within +/- 10% of the actual listing price. This ensures that users receive highly accurate price estimates for their desired flats.

2. **Root Mean Square Error (RMSE):** 
   - RMSE will be calculated in monetary terms to quantify the average deviation of the predicted prices from the actual prices. A lower RMSE indicates better model performance and more precise price predictions. We aim to achieve an RMSE below 300.

3. **Data Profiling:**
   - Comprehensive data profiling and analysis will be conducted to ensure the quality and relevance of the data used for model training. This includes checking for missing values, outliers, and ensuring the data's integrity.

These metrics align with the project goals and provide a quantifiable measure of the model's effectiveness in predicting flat prices. They will guide the iterative improvement of the model to ensure it meets the desired accuracy and reliability standards.

## Project Plan
In this project, we will scrape data from the Flatfox.ch website to train a model that predicts flat prices based on parameters like the number of rooms, location, and living space. The process includes:
- Data Scraping: Extract detailed information about flat listings from Flatfox.ch.
- Data Preprocessing: Clean and preprocess the data to handle missing values and normalize features.
- Model Training: Use machine learning algorithms methods to build a predictive model.
- Model Evaluation: Assess the model's performance using relevant metrics to ensure accuracy and reliability.

The goal is to create a tool that helps users estimate flat prices on Flatfox.ch, aiding in their decision-making process.

```mermaid
gantt
    title Data Engineering Project Gantt Chart
    dateFormat  YYYY-MM-DD
    section Planning and Setup
    Project Planning and Setup          :done, 2024-07-01, 1d
    section API Integration
    Research API and Develop Scripts    :done, 2024-07-01, 2d
    section Data Storage
    Setup Database and Schema Design    :done, 2024-07-02, 2d
    section Data Cleaning and Preprocessing
    Data Cleaning and Preprocessing     :done, 2024-07-03, 2d
    section Exploratory Data Analysis
    Exploratory Data Analysis           :done, 2024-07-04, 2d
    section Feature Engineering
    Feature Engineering                 :done, 2024-07-08, 2d
    section Model Development
    Model Development                   :done, 2024-07-09, 3d
    section Model Evaluation
    Model Evaluation                    :done, 2024-07-10, 2d
    section Deployment
    Deployment                          :done, 2024-07-11, 2d
    section Monitoring and Maintenance
    Monitoring and Maintenance          :done, 2024-07-15, 4d

```

## Roles and Contact Details
Authors:

Projekt Lead
Liam Decaster -  [decaslia@students.zhaw.ch]()

Lead Developer
Lukas Wipf  -    [wipflu1@students.zhaw.ch]()

Lead Data Analyst
Grant Gordon -  [gordongr@mail.gvsu.edu]()
