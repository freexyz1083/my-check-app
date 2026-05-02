
import streamlit as st
from datetime import date

st.set_page_config(page_title="毎日のチェック表", page_icon="📋")

st.title("📋 毎日のチェック表")
st.write(f"今日の日付: {date.today()}")

st.subheader("💡 今日の気持ちマインド")
mind = st.text_area("今の心境を書き出してみましょう", placeholder="例：穏やか、やる気に満ちている...")

st.subheader("💎 その気持ちでいる価値")
value = st.text_area("その感情はあなたに何を教えてくれていますか？", placeholder="例：自分を大切にしたいというサイン...")

st.subheader("🐉 自分の中にいる敵")
enemy = st.text_area("行動を邪魔する思考や誘惑は？", placeholder="例：『後でいいや』という甘え...")

if st.button("今日の記録を完了する"):
    st.success("自分と向き合うことができましたね。お疲れ様でした！")
    st.balloons()
