
from transformers import TextIteratorStreamer
from threading import Thread

def summarize_text(model, tokenizer, text, min_length, max_length):
    inputs = tokenizer([text], max_length=1024, truncation=True, return_tensors="pt")
    
    streamer = TextIteratorStreamer(tokenizer, skip_special_tokens=True, clean_up_tokenization_spaces=True)
    
    generation_kwargs = dict(
        input_ids=inputs["input_ids"],
        streamer=streamer,
        min_length=min_length,
        max_length=max_length,
        num_beams=1,           # Beam search doesn't support streaming well, switching to greedy
        do_sample=False,       # Deterministic
        no_repeat_ngram_size=3,
        early_stopping=True,
    )

    thread = Thread(target=model.generate, kwargs=generation_kwargs)
    thread.start()

    try:
        for new_text in streamer:
            yield new_text
    except Exception as e:
        print(f"Error during generation: {e}")
        yield f"[Error: {str(e)}]"

### num_beams=2–4 beams → fast, decent summary.
###             5–8 beams → slower, slightly more polished.
