import os
import translation_agent as ta
import time

if __name__ == "__main__":
    start_time = time.time() # start timer
    source_lang, target_lang, country = "English", "Czech", "United States"

    relative_path = "sample-texts/sample.txt"
    script_dir = os.path.dirname(os.path.abspath(__file__))

    full_path = os.path.join(script_dir, relative_path)

    with open(full_path, encoding="utf-8") as file:
        source_text = file.read()

    print(f"Source text:\n\n{source_text}\n------------\n")
    

    translation = ta.translate(
        source_lang=source_lang,
        target_lang=target_lang,
        source_text=source_text,
        country=country,
    )

    print(f"Translation:\n\n{translation}")


    end_time = time.time()  # End the timer
    elapsed_time = end_time - start_time  # Calculate elapsed time
    print(f"Time taken for the main method: {elapsed_time:.2f} seconds")
