from sklearn.svm  import SVR
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error , accuracy_score , classification_report , r2_score

def model(df):
    x=df.drop(columns=['labels'])
    y=df['labels']
    # train test split
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

    #standardize the features 
    scaler=StandardScaler()
    scaler.fit(x_train)
    x_train_scaled=scaler.transform(x_train)
    m=RandomForestClassifier(n_estimators=100,random_state=42)
    m.fit(x_train_scaled,y_train)

    # prediction on the test set
    y_pred=m.predict(x_test)

    # evaluate the model
    accuracy=accuracy_score(y_test,y_pred)
    classification_rep=classification_report(y_test,y_pred)
    r2=r2_score(y_test,y_pred,multioutput='variance_weighted')
    error=root_mean_squared_error(y_test,y_pred)
    return m,accuracy,classification_rep,r2,error