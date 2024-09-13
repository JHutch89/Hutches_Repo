import pandas as pd

data = pd.DataFrame({
    "Term": [
        "Dep. Variable", "No. Observations", "Model", "Log Likelihood", "AIC (Akaike Information Criterion)", 
        "BIC (Bayesian Information Criterion)", "HQIC (Hannan-Quinn Criterion)", "Covariance Type", 
        "Coefficient (coef)", "Standard Error (std err)", "Z-Value (z)", "P-Value (P>|z|)", 
        "Ljung-Box (Q)", "Jarque-Bera (JB)", "Heteroskedasticity (H)", "Skew", "Kurtosis"
    ],
    "Interpretation": [
        "The dependent variable being predicted by the model.",
        "The total number of observations used in the model.",
        "The SARIMAX model configuration including seasonal order.",
        "Measures how likely the model is to have generated the observed data. Higher is better.",
        "Evaluates model fit with a penalty for the number of parameters. Lower values are better.",
        "Similar to AIC but with a larger penalty for more parameters. Lower is better.",
        "Another criterion for model selection. Lower values indicate a better model.",
        "Describes the method used to estimate the covariance matrix.",
        "The coefficient of the parameter estimated by the model.",
        "The standard error of the estimated parameter. Smaller is better.",
        "The Z-value, which indicates the number of standard deviations the coefficient is from 0.",
        "P-Value for the significance of the Z-value. Should be lower than 0.05 for significance.",
        "Tests if residuals are independent. Higher values indicate no autocorrelation.",
        "Test for normality of residuals. Lower values suggest residuals are normally distributed.",
        "Measures the presence of heteroskedasticity in the residuals. Lower values indicate homoskedasticity.",
        "Measures the asymmetry of the residuals. A value close to 0 is ideal.",
        "Measures the peakedness or flatness of the residuals. A value around 3 is considered normal."
    ],
    "Good Value": [
        "The correct dependent variable", 
        "Depends on the data", 
        "Accurate model specification", 
        "Higher values closer to 0", 
        "Lower is better (e.g., AIC < 2000)", 
        "Lower is better (e.g., BIC < 2010)", 
        "Lower is better (e.g., HQIC < 2005)", 
        "Appropriate choice (e.g., 'opg' or 'robust')", 
        "Coefficients in a reasonable range based on the domain", 
        "Smaller values (closer to 0)", 
        "Values close to 0 (between -2 and 2)", 
        "< 0.05 for statistical significance", 
        "> 0.05 indicates no autocorrelation", 
        "Values closer to 0 indicate normality", 
        "Close to 1 for no heteroskedasticity", 
        "Skew closer to 0 (between -0.5 and 0.5)", 
        "Kurtosis close to 3 is normal"
    ],
    "Recommendations if Unfavorable": [
        "Ensure the correct variable is being predicted.", 
        "Consider increasing the number of observations for more robust modeling.", 
        "Adjust model orders based on data seasonality and lag behavior.", 
        "Re-evaluate model specification and adjust parameters or transformation to improve fit.", 
        "Reduce overfitting by simplifying the model.", 
        "Simplify the model or reduce the number of parameters to avoid overfitting.", 
        "Simplify the model or adjust seasonal components.", 
        "Switch to a different covariance estimator or use 'robust' for heteroskedasticity.", 
        "Review parameter significance or transform variables for better interpretability.", 
        "Smaller standard errors indicate more reliable coefficient estimates; consider improving model fit.", 
        "If Z is too large or too small, it may indicate overestimation or underestimation; recheck parameter specification.", 
        "If P is too high, the variable may not be statistically significant; check for inclusion necessity.", 
        "Increase the model complexity or use differencing to remove autocorrelation.", 
        "Consider transformations or add more data to reduce non-normality.", 
        "Consider using an ARCH/GARCH model to address heteroskedasticity.", 
        "Transform data or improve model specification to fix skew.", 
        "If kurtosis deviates significantly from 3, re-examine model assumptions or try alternative distributions."
    ]
})

# Saving the updated table to CSV for Streamlit usage
path = "Retail_Ops/data_sources/sarimax_glossary.csv"
data.to_csv(path, index=False)