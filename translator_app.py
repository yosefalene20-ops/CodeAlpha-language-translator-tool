import streamlit as st
from deep_translator import MyMemoryTranslator
from io import BytesIO

# Put your real email here: it raises the free daily limit (about 50,000 characters)
EMAIL = "yosefalene20@gmail.com"

st.set_page_config(page_title="Translator", page_icon="🌐", layout="wide")


@st.cache_data
def get_languages():
    t = MyMemoryTranslator(source="english", target="french")
    langs = t.get_supported_languages(as_dict=True)
    return {name.title(): code for name, code in langs.items()}


@st.cache_data(show_spinner=False)
def translate(text, src, tgt):
    return MyMemoryTranslator(source=src, target=tgt, email=EMAIL).translate(text)



LANGS = get_languages()
NAMES = sorted(LANGS)

# ---------- state ----------
st.session_state.setdefault("src", "English" if "English" in NAMES else NAMES[0])
st.session_state.setdefault("tgt", "French" if "French" in NAMES else NAMES[1])
st.session_state.setdefault("input_text", "")
st.session_state.setdefault("result", "")


def swap():
    st.session_state.src, st.session_state.tgt = (
        st.session_state.tgt,
        st.session_state.src,
    )
    st.session_state.input_text = st.session_state.result
    st.session_state.result = ""


def clear():
    st.session_state.input_text = ""
    st.session_state.result = ""


# ---------- UI ----------
st.markdown("<h1 style='text-align:center'>🌐 Language Translator</h1>", unsafe_allow_html=True)
st.write("")

left, mid, right = st.columns([5, 1, 5], vertical_alignment="bottom")
left.selectbox("From", NAMES, key="src")
mid.button("⇄", on_click=swap, use_container_width=True, help="Swap languages")
right.selectbox("To", NAMES, key="tgt")

box_l, box_r = st.columns(2, gap="large")
with box_l:
    text = st.text_area(
        "Enter text",
        key="input_text",
        height=250,
        max_chars=500,
        placeholder="Type or paste text here (max 500 characters)...",
        label_visibility="collapsed",
    )
with box_r:
    if st.session_state.result:
        st.code(st.session_state.result, language=None, wrap_lines=True)  # copy icon built in
    else:
        st.text_area(
            "Translation",
            value="",
            height=250,
            disabled=True,
            placeholder="Translation appears here...",
            label_visibility="collapsed",
        )

b1, b2, _ = st.columns([1, 1, 4])
go = b1.button("Translate", type="primary", use_container_width=True)
b2.button("Clear", on_click=clear, use_container_width=True)

if go:
    if not text.strip():
        st.warning("Please enter some text.")
    elif st.session_state.src == st.session_state.tgt:
        st.warning("Please choose two different languages.")
    else:
        try:
            with st.spinner("Translating..."):
                st.session_state.result = translate(
                    text,
                    LANGS[st.session_state.src],
                    LANGS[st.session_state.tgt],
                )
            st.rerun()
        except Exception as e:
            st.error("Translation failed. Please check your internet connection and try again.")
