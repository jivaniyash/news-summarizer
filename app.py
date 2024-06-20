import gradio as gr
from functions.main import summarizer

description = '''
<div style="display: flex;">
    <div style="flex: 1; margin-top: 15px; margin-right: 10px;">
        <p style="font-size: 1.4em; font-weight: bold;">
            News Article Summarization Demo - provides a Summary of the news article based on the selected tone & character limit.
        </p>
    </div>
</div>
'''

article ='''
<body>
<center>
  <p>Source Code can be found on <a href="https://github.com/jivaniyash/news-summarizer"> GitHub.</p>
</center>
</body>
'''

demo = gr.Interface(fn=summarizer, 
                    inputs=[gr.Dropdown(["World", "Business", "Sports", "Health"], label="Select News Category"),
                            gr.Textbox(label="Date", lines=1, placeholder="Please enter Date in MM-DD-YYYY Format", info="eg.06-18-2024"),
                            gr.Textbox(label="Character Limit", placeholder="This is the output limit. Please enter a number. eg.150"),
                            gr.Dropdown(["Formal", "Informal", "Inspirational", "Humorous", "Sarcastic"], label="Select Output Tone")],
                    outputs=[gr.Textbox(label="News Article", lines = 7, max_lines=7, autoscroll=True),
                            gr.Textbox(label="Summary", lines=5)],
                    # title=title,
                    description=description,
                    article=article,
                    # examples=[["Business", "06-17-2024", "250", "Formal"], 
                    #           ["Health", "06-20-2024", "300", "Sarcastic"]],
                    # cache_examples=True,
                    allow_flagging="never",
                    theme="default",
                    clear_btn= "Clear")

if __name__ == "__main__":
    demo.launch(share=False, debug=True)
