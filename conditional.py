def main():
    x, y = 1000, 100

    if x < y:
        result = "X is less than y"
    else: 
        result = "X is greater than y"

    print(result)  


value = "One"

match value.lower():
    case "one":
        result = 1
    case "two":
        result = 2
    case "three":
        result = 3
    case "four":
        result = 4

print(result) 


if __name__ == "__main__":
    main()
