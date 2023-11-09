In the process of retouching the freshly pdf-to-text scraped stories to make them usable, aside from formatting, certain content-level edits were also made. These "editorial decisions" were deemed necessary to make the text usable, but inevitably required some amount of discretion and subjectivity. Extremely routine kinds of edits were not recorded, but for most of these editorial decisions, I recorded the exact list of IDs of affected stories. I have recorded these edits not only for transparency of methodology, but to explain my reasoning for having made these edits, especially for if these decisions need to be revisited later.

We can distinguish three types of things that can be removed from a story's text:
1. Scraped text which is not at all a component of the story's text
    - e.g. page numbers, the author byline, the word count
2. Scraped text which is a component of the story's text yet clearly not itself a part of the story's literal words
3. Scraped text which is itself a part of the story's literal words, but (arguably) not part of the story's sentences.

So called "editorial decisions" affect mostly class 3, but also class 2. These classes are also in practice not rigid distinctions, and any particular element could controversially be put into any category, and the category under which the same element falls may depend on the particular story at hand. For example, one could argue that the title of a story could belong to any of these classes: for some stories the title may be nondescriptive or minimally relevant, landing in class 1; in some stories the title may be part of the experience of the story by setting or subverting expectations, landing in class 2; in some short stories the title may be understood as being an opening sentence of the story, landing in class 3.

Note finally that these editorial decisions are just for manual processing of the texts (going from `texts` to `retouched_texts`) and do not include any of the changes that were performed to format the texts and make them usable (from `retouched_texts` to `ascii_texts`). The script `clean_whitespace.py` and the effects of the commandline tool `konwert` are all that is at play there.

### General Decisions affecting all stories:

The story title is removed.

Author bylines are removed.

Content/trigger warning tags are removed.

Word counts are removed.

Running headers are removed. This includes page numbers, but potentially other things too, like if the title or author byline are reprinted.

Author contact information (phone number, address, email, etc.) is removed.

Section dividers are removed (e.g. * * * * * * *, -----, ###, *, ...., ..., etc.)

Chapter titles are removed.


## General categories:


### Stories beginning with a quotation:
Decision: Quote is removed. Reasoning is twofold. For one, the attribution of the quote often messes up sentence formatting. For two, it's not the author's own words.

Argument against: A good epigraph really ought to be percolating in the reader's mind before they open the text. (eg Frankenstein). Its effect therefore is significant. Furthermore, while it is true an author themselves does not write the epigraph, they choose the epigraph and have editorial control over it therefore. Choosing an epigraph may well be as hard as choosing the words for a novel sentence.

Stories affected:
02b74b4e197589b574d9874cf4b36e2d.txt
06b6dd68274d7d4180e84e7bd4d2c77c.txt // in fact it's an entire poem, including a disclaimer from the author that said poem is public domain. It is the author's translation.
06f10aa894b0b39bf5faa14381897320.txt // it appears this story was submitted twice? it has some differences from the above.
0a2dcae5189bbe6e478db9d3d9697ad3.txt // quotation renders out of order for some reason
10517285b6a1a012a443430fa9ea1537.txt // I also adjoin the syllable-broken words
12169f13b56e646f1f1ad854162503c9.txt // the Beatles
17b9863e04b7c612bfa1a9af66487989.txt
1ac9232a862086b2096ca349a9fe80a2.txt // news report
1d16138ca1326f1ada65bbde1a403aea.txt
23fe3ec8c9161d647c98c67de4f86f24.txt
26e84ded28a1d786c6873d7fcb5057f9.txt
28dc56e58852f520acbe968f37ccdb3b.txt // definition of a word
2d028afc91661a357715c6fd39958135.txt
3043b5d136b069ab8ab9ab8bbe679889.txt
30bd10f82ff3bb67447674d33e2d3ef8.txt
3adb9faba06d0c0f1b96514541e5e534.txt // a news article with a link ???
3d26eb6e5a0119691308f7ca5b8a370a.txt // uses a Humans of NY
4275cdef13878c9f41805c02e99431c8.txt
4463057e5a31961a438d6807f7fe5bc7.txt
459210304fcd818cf9db1e11d8a1182e.txt
49d9442fedc61a6f2f9d542102d6e69a.txt // literary forgery quote
532930bf2d5d169c4665ec4d66d111c1.txt
56935dc0f9501b67ff487f3dde235dcb.txt
5d63cb3873e807b60edfe862739e7fb9.txt // word definition
6efd7945bd72e0b4125e4d84811384fc.txt // ee cummings
72b788400ac2342ce97b4c5228258438.txt // shakespeare
7be75201b64d057a5e8953444ae884f7.txt
7eeeb9be1c4a2809219a76e5811964de.txt
82ed84cf3d98c32c0c54a6deaebff884.txt // also has !'s
865b87f6cee6931ee8cea588e9d7dfe3.txt
8f9bbf11c79281b7d4f4b7c0ec14d0de.txt
90370fae0af068d52329e09e551d78dc.txt
a202f407ca10373ef310cb089f70d264.txt // Bible verse
a50945a0845a5510dfa1170b1aee6f8f.txt // opens with a literary forgery, so can be reevaluated
a55e099f07e534da3d310eb3f5715e90.txt // twain
a9c1da2c83e20df50e939989f9982548.txt
a9e6ce664a6250068170166bb1c16789.txt // including a second quote in Arabic
aa5272109f7bd9734d5617a247e222b7.txt
ac436cd8849b23eaca4a5415278a21e9.txt
ad0d52e78fe16af1b22b5030394aa867.txt
b127a14571f39f560aa55978b552c6e6.txt
b45370e4e25c83ba137d2b63f926b243.txt
b7cb0aa88791086e9b882269feb3cdf2.txt
baf33f80be5588fd6a16b02d32ed060a.txt // quote is from a character in-universe but I guess it's still a quote?
bd24cbdf2b63801a48b3853be3bd0f82.txt
bd828ba77c5ac3a0de7f1109a9f52be4.txt
c751b5cab5ce86375aaa9e79e8ae552c.txt
cb3071cd6486fd4d49201ed147eeac35.txt
cc7bae99d63429b41449e52168ec2dda.txt
ccbf1e39da5f6d65d2061e7bd4d204c9.txt // has quote, but also has the first letter of the first line displaced. Manually fixed.
cd140b83579232a8c93bde8d2518d72c.txt
d393d79a377e97892f665cb65f2db770.txt
d6053b9c4464a24fcd1c99a0e296fecc.txt
dcefa02772070e32a0f5c994e153048f.txt
e2d9365c2dc150755f8e5f6a6383cace.txt
e4154a98e493027af644f298cfd4f933.txt
e4cd7e092223c15ec89e4feacd8f5b9f.txt // a hymn
ec0569b768661ff0711313e4ea963d96.txt // nyt article excerpt
f0637c4e1176b6e4019f3d338312c91d.txt // j alfred prufrock
f165e574002603b0c9545ae1f7185e6b.txt // hymn
f31c46332fa9339aef2041463728b327.txt // contains attribution (and uncopied image) to a nyt article
f438e68ede2df22be9f38d4ce35dfc86.txt
f59e5d69b40cc335c4ad5508fdd6b0fd.txt
f9b7f7965df9d65b4b84bfc769b429be.txt
fc3f51e244e047f3f7741ae8ab70464b.txt

Stories NOT affected:
054189c12dc0a8dd7486a1b7c8550e66.txt // this isn't quite an epigraph since it is unattributed and indeed seems to be novel? so I keep it.
070a854327a514db07c0a307a2a6ecbe.txt // it opens with a Dick and Jane forgery (? maybe it's real) but is not presented as a quotation
d06c97ebb9ef0563ae09aa9b5c31b134.txt // kept since the quote is from in-universe


### Stories beginning with a letter:
Decision: For stories that begin to a letter for another person, I decide to remove the header (eg the address of the letter, the date, and the opening line addressing the reader of the letter). Such information messes with the simple heuristic for extracting the first sentence that we wish to build, and moreover isn't really the first sentence conceptually anyway.

Argument against editorial decision: the address of the letter and the person being addressed are sometimes plot critical information; and furthermore they are necessary for contextualizing the first "actual sentence" of the story. One clearly reads a sentence differently if it is text of the story, dialogue, or diegetic text; and this is context that BERT and other LLMs too are likely sensitive to.

Stories affected:
00e2b8739d9319bf3a3895a7df6890d5.txt
07e4ba9705029b39cb108f50333cd0f8.txt // this is presented as an email specifically
17b2166a816470b0f5862f8bdf4798e2.txt // this is a weird case since it has a parenthetical, but I strip it all the same
2091ce121bd292521950206d62320c6b.txt
25e7f16588049bdb908c6f4f5f1376e5.txt
2e67e9baef10587ba3a4f3ad14087e64.txt
4e8136cd5eb07ed8daec6f3e67fd642d.txt // it is addressed to a king, which is maybe important storywise. Oh well.
510b5cce565e6b48027eacc2e4d25683.txt
62d9f83167cd1dc54fce4c27e4f98baf.txt
9b132df5468f9fcc8fe2f306ccda03e4.txt // presented as a training manual
9f036a07ef2e3c5ffa20ecf952d614b5.txt
c5c808a551d88bdbad03eb48ad1f3975.txt // entire story is a letter
cc5713d8e9d772d146e5e9bb33d2819f.txt // presented as an email
d012b2ee7586d7b88e4dbb7fc96240e8.txt // this begins with a text prefaced by "You have a message from [user]!". I decided to delete that line since it functions like "Dear X" conceptually
d769bc9f99e4ef90490bf3875b657e64.txt // writes who the narrator is, which feels conceptually similar
e2f1cf2ebafe49692b55a33d885d6350.txt
f2b4d964567b3cc5ea2553addf6d2d13.txt // framed as a diary entry

### Stories beginning with a time/place:
Decision: remove the date. Reasoning analogous to stories beginning with a letter.

Argument against: Reasoning analogous to stories beginning with a letter.

Stories affected: (non-comprehensive, i do this reflexively now)
0298f0d1c15a2c7a7649312f653a46d9.txt
0d292514139b686b69a84b0e2a159e0e.txt
1600c517c771422de59f17382793afb9.txt
16421e18fb0d1d00de2f724c9fb909f1.txt
175706a8f227ce0890d7d6a7ca4d2f18.txt
a1f5ec714448b2896befd868e0ba4072.txt // this one's a bit odd since it has some imagery in the setting
a3afdc1660f4f45e760e8471add1052c.txt
a67e28f39ae5a17ebfb7f5d757ed650d.txt
7ac847befad7477aef242d0797bc0ccd.txt
994bfcf1317e37adc18af5f452c1bce2.txt // date and place

### Stories with content warning
Decision: remove content warning

affected:
49987679e09f8cfcbdbb27804077d39f.txt

### Stories beginning with an author's note or summary or dedication
Decision: remove the author's note

affected:
14abaa0950dda1947f46641132371748.txt
14c7a8500069057471b34f01cd11c75c.txt
182c66e867a28f3fe36d17a51a54ee1c.txt
385691f8f9fac9ff140648b9545a1440.txt // has a dedication
3b87805869dcdf0c3e05a7d97b061d3a.txt
497121f48466bc4d045f43ea444fe731.txt // dedication
4c16e7c70f9d10aff847d3ef3faebfe0.txt
68b4756595f7496eec451f7eb6741efc.txt // historical context
6a08f1d730b6894a6e6b99025feca7d0.txt // history
6f127b9c8109e249677a662fd9d1f80c.txt // weird stuff idk
71dc076ca407469a1ea270a15c1feeed.txt
75abffa3548b7b669da04c3234aa59cd.txt // explanation of Japanese mythology
800c93b0635dfd192eedf2fcdf96c6c8.txt // lots of forgery quotes
8388524364d35da5a9d5b7693bd59187.txt // weird preface idk
874b90d1db6b6e0f0f771b23d061d2a5.txt
8be6a36b3801b0d0d72aeda7ce418259.txt // history
8d696663e330aab26ff59d787270edc3.txt // defn
97f1d498cada5b2a6a10ac6e65958735.txt // framed as literary forgery
a2509f4d8adbb35c07b012af0ce621d4.txt // odd that it still has a preface ultimately but eh
78588eae26913300ae8cec5823aeedda.txt // author dedication
bbeb4f4f26057a01501a288896d9a2f0.txt // this opens with a literary dedication to two real life figures? (Chuine [sic] Sugihara and Raoul Gustaf Wallenberg: Japanese diplomat and Swedish architect, each of whom saved Jews in the holocaust). I remove it since it seems to be in the author's own voice, but on the other hand it seems likely it bears upon the meaning of the story.
bfdacb21c86d3134b28e5e9518f05450.txt // word definition (with attribution)
c05b47e4b561e07f43f098bfb83fe18f.txt // has a table of contents (and a letter for the first section)
c80b3dedea488ea09cdddde6857cfb7e.txt // something about the story and string theory
c8aa27069dc65fb7b23d27ac0bdd0de8.txt // opens with an in-universe dialogue, but I delete it for formatting reasons (I also delete a weather report afterwards)
d0dacd6372f5540c48b93b4ade5f60f8.txt
d2b02fb9c8b062d9a03b8510d80f86d8.txt
d572fc93b039b063dd05fd5ba4e487d1.txt
ddca4c36a7005082d3efd11b523d31af.txt // summary
e22e0f9a573ecaa325ca27329b5ec5d2.txt // a literary dedication, but a dedication nonetheless
e590b3cdce2da3be1892b1252d351ecc.txt // author notes their prior submission and the completion of changes
ed111701c9e760d60be7de2017b8154b.txt // unclear what to do with this frankly difficult to read opening address (in the style of Shakespeare; not sure what the word for this kind of thing is). I decided to remove it.
ed54e2f47194524c8eb14d17ca5ee422.txt // has a very brief author bio


exceptions:
2e96d5c895bd97f54bb17cb93f07b6cc.txt // this summary has a more fictive, poetic quality to it that the others don't, so I keep it.
31aadf23f30f9b70efc9e9779bd9c99d.txt
52b216d406589230aa4847aea4c31d05.txt
54d5c4c0183d851ecbd1653b6007a76a.txt // again, has a fictive quality
5c846d23e4984abbf2d215b02b244e70.txt // honestly this was a mistake that i skipped over, maybe I will remove it later
70942fa28c8d84991abe11f90c1b88bd.txt // weird kind of scientific definitional summary
a833e3abdd4b5a6ba7e291d8da668db3.txt // though it looks like an author's note since it's fourth wall breaking, the foreword is a forgery and diegetic, and therefore kept




### No decision yet rendered
This category is for stories where the right approach is not immediately obvious. I put stories here to table them.

0408ae6ba68d626e63a98596e170a19a.txt // This story begins with a countdown (like a rocket launch countdown). Should I remove the numbers?
762c19f829dd2be06126f5438bd04175.txt // it's a dialogue with dashes between. I removed the dashes though

### Story empty
Empty stories may sometimes have a few characters of text. I actually empty the files so that they can be discarded more easily later.

0aa8659bf3cc86ccff5117517fb40d73.txt
0badc41d20da2686218bba89bfea2893.txt
112b5f5563c26d9a441b6b46be7173dd.txt
146d5fd7d3149e4684ea3ffab3b2c368.txt
384af2582d2a1d00bedf0f6915e4d6a4.txt // the author withdrew the story by uploading a new pdf that was blank and said "story withdrawn"
422c2158ac3d5f5b5bb5a14f1cf62f91.txt
46ee3fb90ed856bfbb8754a35220b9e4.txt
57a1161b4af47a0b2ff1a9aa6d4066ad.txt
58b428f6917acc4454bd7e9268be00e0.txt
6971b6db538dad7d4e7affa6322e0e1b.txt
6b7a2295ff07937bb7ae2406f2fc70c4.txt
6db18401e9bb7590ecf8c2f32ecc3679.txt
7561f790a9c85132c430cbcbab622cab.txt // withdrawn via pdf
8219a71b115eb70bd036c805afe58a57.txt
8a8dfbbefee9282455f929994d0484ae.txt
8d161f5a32365938a97c58b0c195e709.txt
8da23bc1cfdc338a1c3e02e6f4ea30d4.txt
91a97b59b0d92fd0f22ef54a3b081997.txt
99a192ad471b4a0988b8162b07db5244.txt
c2bf97a63d05175c5d5e5fcd60bbef0d.txt // withdrawn via pdf
c7af1e41002c530bb987def8b954c314.txt
d59b178996a9b70712a85ca089585318.txt
e8eb860f21f494ed92ca4c8cd6b49d4c.txt
fb31e5f48b6ce079ebe6a7eb721f9032.txt

### Unusable
This category is for stories where some quirk of formatting makes them a pain to format correctly. I will empty their files as if they were empty or misprocessed, but we can revisit them later.

05ad4525242e83ec349f2349c936402b.txt // the author used a typewriter esque left hand line numbering, so the text is interleaved with random numbers.
08dd3b02c1c4ed7fb0506b261c9eb62b.txt
3975d4f0384b87f4b8f52869483a39f2.txt // left hand numbering
48adbfece6d284022c8db457d28a76b7.txt // `a`'s substituted with `,`
4d2cb6bf682a501e137084b76d8b970a.txt // encoded completely incorrectly
57094f0d1c7477937b1bce7ae3e5815b.txt // opening line has eye dialect stuff? unclear if it's intentional. I just remove it rather than edit the doc in a way the author might have objected to.
6c998fbe13102f6b1cf426722902430a.txt // bad encoding on some words
95d47e1acf2147a6fe239ebbbfa52964.txt // bad spacing
a4bdc34b933ff6e461dfec300f1ee7a5.txt // weird multinested parentheses and spacing
a8699b65c7f9a99a65bb494349acd7ac.txt // digraphs with the letter "f" appear to have been separated from their words?
aa8e8d3fa1476c9f857f072dd4fbfad0.txt // a literary forgery: presented as an Aptitude Test
ae8103daf372feb1d73ac3abb639d233.txt // presented as a dialogue with attributions of the interlocutors
af41f65b03d8bd70a7aeaa7c361f10c4.txt // someone submitted a Lorem Ipsum ...?
bdf6265111f637801892e74a36c017b8.txt // completely transcribed incorrectly, and iirc there exists some story that seems to be untranscribable — maybe this is it.
c06757d14c6d9cd90cdd4e5652ccf920.txt // transcribed profoundly out of order
c6a310ff99cdf9d95e50aaebc294211b.txt // has footnotes. Probably salvageable but not in a way that I am willing to put forward into the dataset at the moment. (Also has an author's note at the beginning to warn about the footnotes' formatting)
c8a62357335e5a7c467c0376342453c9.txt // presented as a museum gallery guide, unclear how to get a (meaningful) first sentence.
d8f59be6fb366662b35851566f2be661.txt // a dialogue
dbc711f10024af83ae9fb26000f6f783.txt // transcribed incorrectly
dc1ccabb35b7d269fed71625c8ca7749.txt // presented as a press release
e980712571657e584fae2044c8eff997.txt // presented as a dialogue

### Questionable usability
I don't empty these files and try to clean up "enough" of the intro to make them usable, but they may have problems. Should be scrutinized more.

1a0253003ce16868f0a6e0e61a264a3a.txt // I cleaned it up a bit but there is gratuitous use of en dashes that may stymie a tokenizer
1f3c2a9790232a3b4cc2beec31043149.txt // worked on it a bit; there are exclamation points separating many lines. Also had a quotation.
20adeffa8540b16faa4de22567326cc6.txt // ! between lines
23d289c254fd72ff6280dd54bfbde98b.txt // ! btwn lines
278092904aedc088dd4e32f33a88df6e.txt // [np] everywhere for some reason, but I've removed them all so it should be ok
391d3f7e66586e0056174c8c8afc954e.txt // I cleaned up the very first sentence, but overall this is presented as a dialogue with name attributions, like in a play or a visual novel. Probably not usable.
39bfc07996be85aea161fcc6d36807aa.txt // ! btwn lines
45351aa121df9cbda3ed28930f8e21f7.txt // has a quote from the rubaiyat and also sporadic dating... honestly is also like a poem in form, maybe should be shelved.
48aaba97268daddd6634001b0a376454.txt // should be okay, but for some reason many grafs are begun with "Table X"
4c18238509bf30c14cd0285c38401e4f.txt // lots of tabs for some reason but should be okay
4c22ea5143fe07188e3ce395f40faee4.txt // ! btwn lines
4d18903a409af1797576c8d10b492cd3.txt // this looks like poetry?
517d433ebd051f313fce09484ff21360.txt // should be okay but this story in general is intercalated with many quotes
5d7cb34bac64b2e7db2146d633ebb370.txt // should be okay but lots of quotes
59ae3437b981863aa78f2b728363a0ba.txt // missing unicode character in there but it can be find-and-replaced as `Th`
76ae71dfa2c96d7a86d4bea5655f0dd9.txt // should be okay but lots of spaces
7a5f81c6511bc89678cf3091ee0a0b15.txt // weird enumeration i removed
9765ef819935d66afc559e60fbf97660.txt // !'s
99fff0ba383fb8ec7dc5aba87fce2364.txt // weird
a94490bac7fddf987a8e81a6eb5f6f42.txt // probably okay but this story for one has some innovative uses of brackets (eg "your[true]self") and, more problematically, includes footnotes. I've removed the footnotes for the first page so we can extract at least the first few sentences, but removing both the numbers and the actual footnotes themselves may prove problematic. The story also begins in the middle of a sentence (should the title be kept as part of the sentence?) but oh well. I might revisit this decision and nix it honestly.
aabaa0c3ee544daac1bea59766ba9af9.txt // a literary forgery; presented as a patent. I've removed the patent copperplate and the numerals, but it's still not really formatted as a story.
af98bbc095d6a9020f2d0043a7a28984.txt // there are errant quote marks but this is easily solved or ignored by a good tokenizer; it's probably okay?
bf041de714fef90f748cad0329681563.txt // presented as a dialogue
bfc6a9c20ba13e6e20e2297a5e0082a4.txt // presented as a biblical dialogue with polysyndeton
cc80498fb441367d2efc88782551877c.txt // this took a couple of find-and-replaces but I was able to quickly clean it up, should be usable (TODO go back and redo regex with \d+ instead of \d*)
cfcf735dfe7b46290e240077f10fba7f.txt // contains some illegally incoded characters, but not in the first 50 or so lines so we should be fine?
d06fbfb776c2f428c7cf422fdedff2c7.txt // each line of dialogue has a hyphen before it, but a tokenizer should take care of it?
d37cd61ede387325bcdd78a0b7c0b9f9.txt // again with `a`'s substituted with `"`; but there are no quotes in the actual story so it cleans up easily
d42b6a5e64352602363f7c3d002d4ce0.txt // exclamations at end of lines but cleans up easily
d8a179c9f0d1cbf78989791eb75fad8c.txt // seems to have a poem at the beginning before the title, which I removed, but examining the pdf the entire content is poems? So unclear if I should have kept it.
e21ac2828d56c75da9b58fe991cfa8e6.txt // presented as enumerated diary entries. Lots of numbered lists — would this interfere too much with tokenization?
ea803a2789cf9c87147d3a59a276aec1.txt // this is a collection of the author's work: several poems and one short story. I excise the poems and keep the short story.
