def model_result_set_to_json(result_set):
    """
    Marsharll a model result set to JSON
    Assumes that model has a to_dict() method
    """
    import json
    return json.dumps([r.to_dict() for r in result_set])
