from sklearn.metrics import log_loss, roc_auc_score

__all__ = ["evaluate_and_save_results"]

def evaluate_and_save_results(model, test_model_input, test):
    # 예측 및 평가
    pred_ans = model.predict(test_model_input, batch_size=256)
    print("test LogLoss", round(log_loss(test['target'].values, pred_ans), 4))
    print("test AUC", round(roc_auc_score(test['target'].values, pred_ans), 4))

    # 예측 결과 저장
    test['pred'] = pred_ans
    result_df = test[['userId', 'title', 'pred']]
    result_df.to_csv('movie_recommendations.csv', index=False)
