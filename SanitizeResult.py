# for sanitize detection result
import json


def SanitizeYOLOResult(results):
    sanitized_result = []
    for result in results:
        _position = []
        for i, position in enumerate(result[2]):
            _position.append(position)
        _result = {
            'name': result[0].decode(),
            'confidence': result[1],
            'position': _position
        }
        sanitized_result.append(_result)
    return json.dumps(sanitized_result)


def CombineResults(diff_list, yolo_list):
    combined_result = {
        'detected': [],
        'unknown': []
    }
    for diff in diff_list:
        combined_result['unknown'].append(diff)
    return combined_result
