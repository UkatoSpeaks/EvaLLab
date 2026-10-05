import json

from app.llm import generate_answer


def load_dataset():
    with open("app/datasets/support.json", "r", encoding="utf-8") as file:
        return json.load(file)


def main():
    dataset = load_dataset()

    for item in dataset:
        answer = generate_answer(item["question"])

        print("=" * 60)
        print(f"ID: {item['id']}")
        print(f"Question: {item['question']}")
        print(f"Expected: {item['expected_answer']}")
        print(f"Actual:   {answer}")


if __name__ == "__main__":
    main()