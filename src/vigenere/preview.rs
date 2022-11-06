use dioxus::prelude::*;
use super::key::VinegereKey;


#[inline_props]
pub fn Preview(cx: Scope, txt: String, vinkey: UseRef<VinegereKey>) -> Element {
    let upperText = txt.to_uppercase();
    let chrs = upperText.as_bytes().iter().map(|v| (v - 65) % 26);
    let nstring = String::from_utf8(chrs.enumerate().map(|(idx, v)| (v + vinkey.read().key[idx % vinkey.read().key.len()]) % 26 + 65).collect()).unwrap();
    cx.render(rsx!(
        "{nstring}"
    ))
}