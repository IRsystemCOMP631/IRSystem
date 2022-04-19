
class Sentiment:
    """
    pip install azure-ai-textanalytics
    pip install azure-core
    """
    _key = "869a01698ffe428f8ee938d3c20ea09c"
    _endpoint = "https://movie-sentiment.cognitiveservices.azure.com/"

    def get_sentiment(self, doc):
        from azure.core.credentials import AzureKeyCredential
        from azure.ai.textanalytics import TextAnalyticsClient
        credential = AzureKeyCredential(self._key)
        text_analytics_client = TextAnalyticsClient(endpoint=self._endpoint,
                                                    credential=credential)
        response = text_analytics_client.analyze_sentiment(doc, language="en")
        return response






