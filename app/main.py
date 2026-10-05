import json

from app.llm import generate_answer
from app.evaluator import exact_match, contains_expected


def load_dataset():
    with open("app/datasets/support.json", "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    dataset = load_dataset()

    for item in dataset:
        answer = generate_answer(item["question"])

        exact = exact_match(
            answer,
            item["expected_answer"]
        )

        contains = contains_expected(
            answer,
            item["expected_answer"]
        )

        print("=" * 60)
        print(f"ID: {item['id']}")
        print(f"Question: {item['question']}")
        print(f"Expected: {item['expected_answer']}")
        print(f"Actual:   {answer}")
        print(f"Exact Match: {exact}")
        print(f"Contains Expected: {contains}")


if __name__ == "__main__":
    main()