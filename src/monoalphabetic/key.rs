use dioxus::prelude::*;

#[derive(Debug, Clone)]
pub struct MonoalphabeticKey(pub [Option<u8>; 26]);

impl MonoalphabeticKey {

    pub fn empty() -> Self {
        Self( [None; 26] )
    }

    pub fn encode(&self, c: usize) -> Option<u8> { self.0[c] }
    pub fn deocde(&self, c: u8) -> Option<u8> {
        for (idx, dm) in self.0.iter().enumerate() {
            if let Some(v) = dm {
                if *v == c {
                    return Some(idx as u8);
                }
            }
        }
        
        None
    }

}

#[inline_props]
pub fn KeyEditor(cx: Scope, monokey: UseRef<MonoalphabeticKey>) -> Element {
    let key = monokey.read();

    cx.render(rsx!(
        table {
            border_spacing: "0px",
            tr {
                (0..26).map(|v| {
                    let chr = String::from_utf8(vec![v + 65]).unwrap();
                    rsx!( "{chr}" )
                })
            }
            (0..26).map(|range| {
                let k = key.encode(range as usize);
                let nk = key.clone();
                rsx!(
                    tr {
                        padding: "0px",
                        margin: "0px",
                        (0..26).map(|domain| {
                            let decodes = match k {
                                Some(v) => v != domain,
                                None => false
                            };
                            let encode = nk.deocde(domain);
                            let encodes = match encode.clone() {
                                Some(v) => v != range,
                                None => false
                            };
                            let disabled = if decodes || encodes { "true" } else { "false" };
                            let letter = String::from_utf8(vec![65+domain]).unwrap();
                            rsx!(
                                button {
                                    disabled: "{disabled}",
                                    onclick: move |_| {
                                        let old: Option<u8> = encode;
                                        
                                        monokey.write().0[range as usize] = match old {
                                            Some(_) => None,
                                            None => Some(domain),
                                        }
                                    },
                                    width: "26px",
                                    height: "26px",
                                    margin: "0px",
                                    padding: "0px",
                                    border_radius: "0px",
                                    border: "0px",
                                    "{letter}"
                                }
                            )
                        })
                    }
                )
            })
        }
    ))
}
