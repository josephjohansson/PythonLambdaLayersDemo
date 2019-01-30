import my_functions as mf
def layers_test(event, context):
    mf.my_function()
    return {
        'statusCode': 200,
        'body': 'This is a lambda layers demo'
    }