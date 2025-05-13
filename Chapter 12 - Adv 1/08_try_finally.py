def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("Hey, I am inside finally block")
        
        
main()


# We cannot print anything after executing return statement in func() but finally is only the block which executes after return value