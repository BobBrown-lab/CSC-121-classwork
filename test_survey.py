
from survey import AnonymousSurvey

def test_store_single_response():
    """test for single response storage"""
    question = ("What language did you first learn to speak?")
    language_survey = AnonymousSurvey(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses