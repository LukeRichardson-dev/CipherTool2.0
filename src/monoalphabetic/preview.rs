use dioxus::prelude::*;

use super::key::MonoalphabeticKey;

#[inline_props]
pub fn Preview(cx: Scope, plaintext: String, monokey: UseRef<MonoalphabeticKey>) -> Element {
    let k = monokey.read().0;
    let encoded = String::from_utf8(
        plaintext
            .to_uppercase()
            .as_bytes()
            .iter()
            .map(|v| {
                if *v >= 65 && *v < 91 {
                    if let Some(n) = k[(*v - 65) as usize] { return n + 65 }
                }

                *v
            })
            .collect::<Vec<u8>>()
    ).unwrap();

    cx.render(rsx!("{encoded}"))
}