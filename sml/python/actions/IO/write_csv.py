
def handle_write_csv(df, name):
    df.to_csv(name, header = True, index = False)

    return None
