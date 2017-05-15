<!DOCTYPE html>
<html>
  <head>
      <meta charset="utf-8" />
      <title>tuan5_lab</title>
      <style>.markdown-preview:not([data-use-github-style]) { padding: 2em; font-size: 1.2em; color: rgb(56, 58, 66); overflow: auto; background-color: rgb(250, 250, 250); }
.markdown-preview:not([data-use-github-style]) > :first-child { margin-top: 0px; }
.markdown-preview:not([data-use-github-style]) h1, .markdown-preview:not([data-use-github-style]) h2, .markdown-preview:not([data-use-github-style]) h3, .markdown-preview:not([data-use-github-style]) h4, .markdown-preview:not([data-use-github-style]) h5, .markdown-preview:not([data-use-github-style]) h6 { line-height: 1.2; margin-top: 1.5em; margin-bottom: 0.5em; color: rgb(0, 0, 0); }
.markdown-preview:not([data-use-github-style]) h1 { font-size: 2.4em; font-weight: 300; }
.markdown-preview:not([data-use-github-style]) h2 { font-size: 1.8em; font-weight: 400; }
.markdown-preview:not([data-use-github-style]) h3 { font-size: 1.5em; font-weight: 500; }
.markdown-preview:not([data-use-github-style]) h4 { font-size: 1.2em; font-weight: 600; }
.markdown-preview:not([data-use-github-style]) h5 { font-size: 1.1em; font-weight: 600; }
.markdown-preview:not([data-use-github-style]) h6 { font-size: 1em; font-weight: 600; }
.markdown-preview:not([data-use-github-style]) strong { color: rgb(0, 0, 0); }
.markdown-preview:not([data-use-github-style]) del { color: rgb(94, 97, 110); }
.markdown-preview:not([data-use-github-style]) a, .markdown-preview:not([data-use-github-style]) a code { color: rgb(82, 111, 255); }
.markdown-preview:not([data-use-github-style]) img { max-width: 100%; }
.markdown-preview:not([data-use-github-style]) > p { margin-top: 0px; margin-bottom: 1.5em; }
.markdown-preview:not([data-use-github-style]) > ul, .markdown-preview:not([data-use-github-style]) > ol { margin-bottom: 1.5em; }
.markdown-preview:not([data-use-github-style]) blockquote { margin: 1.5em 0px; font-size: inherit; color: rgb(94, 97, 110); border-color: rgb(209, 209, 210); border-width: 4px; }
.markdown-preview:not([data-use-github-style]) hr { margin: 3em 0px; border-top: 2px dashed rgb(209, 209, 210); background: none; }
.markdown-preview:not([data-use-github-style]) table { margin: 1.5em 0px; }
.markdown-preview:not([data-use-github-style]) th { color: rgb(0, 0, 0); }
.markdown-preview:not([data-use-github-style]) th, .markdown-preview:not([data-use-github-style]) td { padding: 0.66em 1em; border: 1px solid rgb(209, 209, 210); }
.markdown-preview:not([data-use-github-style]) code { color: rgb(0, 0, 0); background-color: rgb(234, 234, 235); }
.markdown-preview:not([data-use-github-style]) pre.editor-colors { margin: 1.5em 0px; padding: 1em; font-size: 0.92em; border-radius: 3px; background-color: rgb(240, 240, 240); }
.markdown-preview:not([data-use-github-style]) kbd { color: rgb(0, 0, 0); border-width: 1px 1px 2px; border-style: solid; border-color: rgb(209, 209, 210) rgb(209, 209, 210) rgb(193, 193, 194); background-color: rgb(234, 234, 235); }
.markdown-preview[data-use-github-style] { font-family: "Helvetica Neue", Helvetica, "Segoe UI", Arial, freesans, sans-serif; line-height: 1.6; word-wrap: break-word; padding: 30px; font-size: 16px; color: rgb(51, 51, 51); overflow: scroll; background-color: rgb(255, 255, 255); }
.markdown-preview[data-use-github-style] > :first-child { margin-top: 0px !important; }
.markdown-preview[data-use-github-style] > :last-child { margin-bottom: 0px !important; }
.markdown-preview[data-use-github-style] a:not([href]) { color: inherit; text-decoration: none; }
.markdown-preview[data-use-github-style] .absent { color: rgb(204, 0, 0); }
.markdown-preview[data-use-github-style] .anchor { position: absolute; top: 0px; left: 0px; display: block; padding-right: 6px; padding-left: 30px; margin-left: -30px; }
.markdown-preview[data-use-github-style] .anchor:focus { outline: none; }
.markdown-preview[data-use-github-style] h1, .markdown-preview[data-use-github-style] h2, .markdown-preview[data-use-github-style] h3, .markdown-preview[data-use-github-style] h4, .markdown-preview[data-use-github-style] h5, .markdown-preview[data-use-github-style] h6 { position: relative; margin-top: 1em; margin-bottom: 16px; font-weight: bold; line-height: 1.4; }
.markdown-preview[data-use-github-style] h1 .octicon-link, .markdown-preview[data-use-github-style] h2 .octicon-link, .markdown-preview[data-use-github-style] h3 .octicon-link, .markdown-preview[data-use-github-style] h4 .octicon-link, .markdown-preview[data-use-github-style] h5 .octicon-link, .markdown-preview[data-use-github-style] h6 .octicon-link { display: none; color: rgb(0, 0, 0); vertical-align: middle; }
.markdown-preview[data-use-github-style] h1:hover .anchor, .markdown-preview[data-use-github-style] h2:hover .anchor, .markdown-preview[data-use-github-style] h3:hover .anchor, .markdown-preview[data-use-github-style] h4:hover .anchor, .markdown-preview[data-use-github-style] h5:hover .anchor, .markdown-preview[data-use-github-style] h6:hover .anchor { padding-left: 8px; margin-left: -30px; text-decoration: none; }
.markdown-preview[data-use-github-style] h1:hover .anchor .octicon-link, .markdown-preview[data-use-github-style] h2:hover .anchor .octicon-link, .markdown-preview[data-use-github-style] h3:hover .anchor .octicon-link, .markdown-preview[data-use-github-style] h4:hover .anchor .octicon-link, .markdown-preview[data-use-github-style] h5:hover .anchor .octicon-link, .markdown-preview[data-use-github-style] h6:hover .anchor .octicon-link { display: inline-block; }
.markdown-preview[data-use-github-style] h1 tt, .markdown-preview[data-use-github-style] h2 tt, .markdown-preview[data-use-github-style] h3 tt, .markdown-preview[data-use-github-style] h4 tt, .markdown-preview[data-use-github-style] h5 tt, .markdown-preview[data-use-github-style] h6 tt, .markdown-preview[data-use-github-style] h1 code, .markdown-preview[data-use-github-style] h2 code, .markdown-preview[data-use-github-style] h3 code, .markdown-preview[data-use-github-style] h4 code, .markdown-preview[data-use-github-style] h5 code, .markdown-preview[data-use-github-style] h6 code { font-size: inherit; }
.markdown-preview[data-use-github-style] h1 { padding-bottom: 0.3em; font-size: 2.25em; line-height: 1.2; border-bottom: 1px solid rgb(238, 238, 238); }
.markdown-preview[data-use-github-style] h1 .anchor { line-height: 1; }
.markdown-preview[data-use-github-style] h2 { padding-bottom: 0.3em; font-size: 1.75em; line-height: 1.225; border-bottom: 1px solid rgb(238, 238, 238); }
.markdown-preview[data-use-github-style] h2 .anchor { line-height: 1; }
.markdown-preview[data-use-github-style] h3 { font-size: 1.5em; line-height: 1.43; }
.markdown-preview[data-use-github-style] h3 .anchor { line-height: 1.2; }
.markdown-preview[data-use-github-style] h4 { font-size: 1.25em; }
.markdown-preview[data-use-github-style] h4 .anchor { line-height: 1.2; }
.markdown-preview[data-use-github-style] h5 { font-size: 1em; }
.markdown-preview[data-use-github-style] h5 .anchor { line-height: 1.1; }
.markdown-preview[data-use-github-style] h6 { font-size: 1em; color: rgb(119, 119, 119); }
.markdown-preview[data-use-github-style] h6 .anchor { line-height: 1.1; }
.markdown-preview[data-use-github-style] p, .markdown-preview[data-use-github-style] blockquote, .markdown-preview[data-use-github-style] ul, .markdown-preview[data-use-github-style] ol, .markdown-preview[data-use-github-style] dl, .markdown-preview[data-use-github-style] table, .markdown-preview[data-use-github-style] pre { margin-top: 0px; margin-bottom: 16px; }
.markdown-preview[data-use-github-style] hr { height: 4px; padding: 0px; margin: 16px 0px; border: 0px none; background-color: rgb(231, 231, 231); }
.markdown-preview[data-use-github-style] ul, .markdown-preview[data-use-github-style] ol { padding-left: 2em; }
.markdown-preview[data-use-github-style] ul.no-list, .markdown-preview[data-use-github-style] ol.no-list { padding: 0px; list-style-type: none; }
.markdown-preview[data-use-github-style] ul ul, .markdown-preview[data-use-github-style] ul ol, .markdown-preview[data-use-github-style] ol ol, .markdown-preview[data-use-github-style] ol ul { margin-top: 0px; margin-bottom: 0px; }
.markdown-preview[data-use-github-style] li > p { margin-top: 16px; }
.markdown-preview[data-use-github-style] dl { padding: 0px; }
.markdown-preview[data-use-github-style] dl dt { padding: 0px; margin-top: 16px; font-size: 1em; font-style: italic; font-weight: bold; }
.markdown-preview[data-use-github-style] dl dd { padding: 0px 16px; margin-bottom: 16px; }
.markdown-preview[data-use-github-style] blockquote { padding: 0px 15px; color: rgb(119, 119, 119); border-left: 4px solid rgb(221, 221, 221); }
.markdown-preview[data-use-github-style] blockquote > :first-child { margin-top: 0px; }
.markdown-preview[data-use-github-style] blockquote > :last-child { margin-bottom: 0px; }
.markdown-preview[data-use-github-style] table { display: block; width: 100%; overflow: auto; word-break: keep-all; }
.markdown-preview[data-use-github-style] table th { font-weight: bold; }
.markdown-preview[data-use-github-style] table th, .markdown-preview[data-use-github-style] table td { padding: 6px 13px; border: 1px solid rgb(221, 221, 221); }
.markdown-preview[data-use-github-style] table tr { border-top: 1px solid rgb(204, 204, 204); background-color: rgb(255, 255, 255); }
.markdown-preview[data-use-github-style] table tr:nth-child(2n) { background-color: rgb(248, 248, 248); }
.markdown-preview[data-use-github-style] img { max-width: 100%; box-sizing: border-box; }
.markdown-preview[data-use-github-style] .emoji { max-width: none; }
.markdown-preview[data-use-github-style] span.frame { display: block; overflow: hidden; }
.markdown-preview[data-use-github-style] span.frame > span { display: block; float: left; width: auto; padding: 7px; margin: 13px 0px 0px; overflow: hidden; border: 1px solid rgb(221, 221, 221); }
.markdown-preview[data-use-github-style] span.frame span img { display: block; float: left; }
.markdown-preview[data-use-github-style] span.frame span span { display: block; padding: 5px 0px 0px; clear: both; color: rgb(51, 51, 51); }
.markdown-preview[data-use-github-style] span.align-center { display: block; overflow: hidden; clear: both; }
.markdown-preview[data-use-github-style] span.align-center > span { display: block; margin: 13px auto 0px; overflow: hidden; text-align: center; }
.markdown-preview[data-use-github-style] span.align-center span img { margin: 0px auto; text-align: center; }
.markdown-preview[data-use-github-style] span.align-right { display: block; overflow: hidden; clear: both; }
.markdown-preview[data-use-github-style] span.align-right > span { display: block; margin: 13px 0px 0px; overflow: hidden; text-align: right; }
.markdown-preview[data-use-github-style] span.align-right span img { margin: 0px; text-align: right; }
.markdown-preview[data-use-github-style] span.float-left { display: block; float: left; margin-right: 13px; overflow: hidden; }
.markdown-preview[data-use-github-style] span.float-left span { margin: 13px 0px 0px; }
.markdown-preview[data-use-github-style] span.float-right { display: block; float: right; margin-left: 13px; overflow: hidden; }
.markdown-preview[data-use-github-style] span.float-right > span { display: block; margin: 13px auto 0px; overflow: hidden; text-align: right; }
.markdown-preview[data-use-github-style] code, .markdown-preview[data-use-github-style] tt { padding: 0.2em 0px; margin: 0px; font-size: 85%; border-radius: 3px; background-color: rgba(0, 0, 0, 0.0392157); }
.markdown-preview[data-use-github-style] code::before, .markdown-preview[data-use-github-style] tt::before, .markdown-preview[data-use-github-style] code::after, .markdown-preview[data-use-github-style] tt::after { letter-spacing: -0.2em; content: " "; }
.markdown-preview[data-use-github-style] code br, .markdown-preview[data-use-github-style] tt br { display: none; }
.markdown-preview[data-use-github-style] del code { text-decoration: inherit; }
.markdown-preview[data-use-github-style] pre > code { padding: 0px; margin: 0px; font-size: 100%; word-break: normal; white-space: pre; border: 0px; background: transparent; }
.markdown-preview[data-use-github-style] .highlight { margin-bottom: 16px; }
.markdown-preview[data-use-github-style] .highlight pre, .markdown-preview[data-use-github-style] pre { padding: 16px; overflow: auto; font-size: 85%; line-height: 1.45; border-radius: 3px; background-color: rgb(247, 247, 247); }
.markdown-preview[data-use-github-style] .highlight pre { margin-bottom: 0px; word-break: normal; }
.markdown-preview[data-use-github-style] pre { word-wrap: normal; }
.markdown-preview[data-use-github-style] pre code, .markdown-preview[data-use-github-style] pre tt { display: inline; max-width: initial; padding: 0px; margin: 0px; overflow: initial; line-height: inherit; word-wrap: normal; border: 0px; background-color: transparent; }
.markdown-preview[data-use-github-style] pre code::before, .markdown-preview[data-use-github-style] pre tt::before, .markdown-preview[data-use-github-style] pre code::after, .markdown-preview[data-use-github-style] pre tt::after { content: normal; }
.markdown-preview[data-use-github-style] kbd { display: inline-block; padding: 3px 5px; font-size: 11px; line-height: 10px; color: rgb(85, 85, 85); vertical-align: middle; border-width: 1px; border-style: solid; border-color: rgb(204, 204, 204) rgb(204, 204, 204) rgb(187, 187, 187); border-radius: 3px; box-shadow: rgb(187, 187, 187) 0px -1px 0px inset; background-color: rgb(252, 252, 252); }
.markdown-preview[data-use-github-style] a { color: rgb(51, 122, 183); }
.markdown-preview[data-use-github-style] code { color: inherit; }
.markdown-preview[data-use-github-style] pre.editor-colors { padding: 0.8em 1em; margin-bottom: 1em; font-size: 0.85em; border-radius: 4px; overflow: auto; }
.scrollbars-visible-always .markdown-preview pre.editor-colors .vertical-scrollbar, .scrollbars-visible-always .markdown-preview pre.editor-colors .horizontal-scrollbar { visibility: hidden; }
.scrollbars-visible-always .markdown-preview pre.editor-colors:hover .vertical-scrollbar, .scrollbars-visible-always .markdown-preview pre.editor-colors:hover .horizontal-scrollbar { visibility: visible; }
.markdown-preview .task-list-item-checkbox { position: absolute; margin: 0.25em 0px 0px -1.4em; }
.markdown-preview code { text-shadow: none; }
.bracket-matcher .region {
  border-bottom: 1px dotted lime;
  position: absolute;
}

.spell-check-misspelling .region {
  border-bottom: 2px dotted rgba(255, 51, 51, 0.75);
}
.spell-check-corrections {
  width: 25em !important;
}

pre.editor-colors {
  background-color: #fafafa;
  color: #383a42;
}
pre.editor-colors .line.cursor-line {
  background-color: rgba(56, 58, 66, 0.05);
}
pre.editor-colors .invisible {
  color: #383a42;
}
pre.editor-colors .cursor {
  border-left: 2px solid #526fff;
}
pre.editor-colors .selection .region {
  background-color: #e5e5e6;
}
pre.editor-colors .bracket-matcher .region {
  border-bottom: 1px solid #526fff;
  box-sizing: border-box;
}
pre.editor-colors .invisible-character {
  color: rgba(56, 58, 66, 0.2);
}
pre.editor-colors .indent-guide {
  color: rgba(56, 58, 66, 0.2);
}
pre.editor-colors .wrap-guide {
  background-color: rgba(56, 58, 66, 0.2);
}
pre.editor-colors .find-result .region.region.region,
pre.editor-colors .current-result .region.region.region {
  border-radius: 2px;
  background-color: rgba(82, 111, 255, 0.2);
  transition: border-color 0.4s;
}
pre.editor-colors .find-result .region.region.region {
  border: 2px solid transparent;
}
pre.editor-colors .current-result .region.region.region {
  border: 2px solid #526fff;
  transition-duration: .1s;
}
pre.editor-colors .gutter .line-number {
  color: #9d9d9f;
  -webkit-font-smoothing: antialiased;
}
pre.editor-colors .gutter .line-number.cursor-line {
  color: #383a42;
  background-color: #f2f2f2;
}
pre.editor-colors .gutter .line-number.cursor-line-no-selection {
  background-color: transparent;
}
pre.editor-colors .gutter .line-number .icon-right {
  color: #383a42;
}
pre.editor-colors .gutter:not(.git-diff-icon) .line-number.git-line-removed.git-line-removed::before {
  bottom: -3px;
}
pre.editor-colors .gutter:not(.git-diff-icon) .line-number.git-line-removed::after {
  content: "";
  position: absolute;
  left: 0px;
  bottom: 0px;
  width: 25px;
  border-bottom: 1px dotted rgba(255, 20, 20, 0.5);
  pointer-events: none;
}
pre.editor-colors .gutter .line-number.folded,
pre.editor-colors .gutter .line-number:after,
pre.editor-colors .fold-marker:after {
  color: #383a42;
}
.syntax--comment {
  color: #a0a1a7;
  font-style: italic;
}
.syntax--comment .syntax--markup.syntax--link {
  color: #a0a1a7;
}
.syntax--entity.syntax--name.syntax--type {
  color: #c18401;
}
.syntax--entity.syntax--other.syntax--inherited-class {
  color: #50a14f;
}
.syntax--keyword {
  color: #a626a4;
}
.syntax--keyword.syntax--control {
  color: #a626a4;
}
.syntax--keyword.syntax--operator {
  color: #383a42;
}
.syntax--keyword.syntax--other.syntax--special-method {
  color: #4078f2;
}
.syntax--keyword.syntax--other.syntax--unit {
  color: #986801;
}
.syntax--storage {
  color: #a626a4;
}
.syntax--storage.syntax--type.syntax--annotation,
.syntax--storage.syntax--type.syntax--primitive {
  color: #a626a4;
}
.syntax--storage.syntax--modifier.syntax--package,
.syntax--storage.syntax--modifier.syntax--import {
  color: #383a42;
}
.syntax--constant {
  color: #986801;
}
.syntax--constant.syntax--variable {
  color: #986801;
}
.syntax--constant.syntax--character.syntax--escape {
  color: #0184bc;
}
.syntax--constant.syntax--numeric {
  color: #986801;
}
.syntax--constant.syntax--other.syntax--color {
  color: #0184bc;
}
.syntax--constant.syntax--other.syntax--symbol {
  color: #0184bc;
}
.syntax--variable {
  color: #e45649;
}
.syntax--variable.syntax--interpolation {
  color: #ca1243;
}
.syntax--variable.syntax--parameter {
  color: #383a42;
}
.syntax--string {
  color: #50a14f;
}
.syntax--string.syntax--regexp {
  color: #0184bc;
}
.syntax--string.syntax--regexp .syntax--source.syntax--ruby.syntax--embedded {
  color: #c18401;
}
.syntax--string.syntax--other.syntax--link {
  color: #e45649;
}
.syntax--punctuation.syntax--definition.syntax--comment {
  color: #a0a1a7;
}
.syntax--punctuation.syntax--definition.syntax--method-parameters,
.syntax--punctuation.syntax--definition.syntax--function-parameters,
.syntax--punctuation.syntax--definition.syntax--parameters,
.syntax--punctuation.syntax--definition.syntax--separator,
.syntax--punctuation.syntax--definition.syntax--seperator,
.syntax--punctuation.syntax--definition.syntax--array {
  color: #383a42;
}
.syntax--punctuation.syntax--definition.syntax--heading,
.syntax--punctuation.syntax--definition.syntax--identity {
  color: #4078f2;
}
.syntax--punctuation.syntax--definition.syntax--bold {
  color: #c18401;
  font-weight: bold;
}
.syntax--punctuation.syntax--definition.syntax--italic {
  color: #a626a4;
  font-style: italic;
}
.syntax--punctuation.syntax--section.syntax--embedded {
  color: #ca1243;
}
.syntax--punctuation.syntax--section.syntax--method,
.syntax--punctuation.syntax--section.syntax--class,
.syntax--punctuation.syntax--section.syntax--inner-class {
  color: #383a42;
}
.syntax--support.syntax--class {
  color: #c18401;
}
.syntax--support.syntax--type {
  color: #0184bc;
}
.syntax--support.syntax--function {
  color: #0184bc;
}
.syntax--support.syntax--function.syntax--any-method {
  color: #4078f2;
}
.syntax--entity.syntax--name.syntax--function {
  color: #4078f2;
}
.syntax--entity.syntax--name.syntax--class,
.syntax--entity.syntax--name.syntax--type.syntax--class {
  color: #c18401;
}
.syntax--entity.syntax--name.syntax--section {
  color: #4078f2;
}
.syntax--entity.syntax--name.syntax--tag {
  color: #e45649;
}
.syntax--entity.syntax--other.syntax--attribute-name {
  color: #986801;
}
.syntax--entity.syntax--other.syntax--attribute-name.syntax--id {
  color: #4078f2;
}
.syntax--meta.syntax--class {
  color: #c18401;
}
.syntax--meta.syntax--class.syntax--body {
  color: #383a42;
}
.syntax--meta.syntax--method-call,
.syntax--meta.syntax--method {
  color: #383a42;
}
.syntax--meta.syntax--definition.syntax--variable {
  color: #e45649;
}
.syntax--meta.syntax--link {
  color: #986801;
}
.syntax--meta.syntax--require {
  color: #4078f2;
}
.syntax--meta.syntax--selector {
  color: #a626a4;
}
.syntax--meta.syntax--separator {
  background-color: #373b41;
  color: #383a42;
}
.syntax--meta.syntax--tag {
  color: #383a42;
}
.syntax--underline {
  text-decoration: underline;
}
.syntax--none {
  color: #383a42;
}
.syntax--invalid.syntax--deprecated {
  color: #000000 !important;
  background-color: #f2a60d !important;
}
.syntax--invalid.syntax--illegal {
  color: #ffffff !important;
  background-color: #ff1414 !important;
}
.syntax--markup.syntax--bold {
  color: #986801;
  font-weight: bold;
}
.syntax--markup.syntax--changed {
  color: #a626a4;
}
.syntax--markup.syntax--deleted {
  color: #e45649;
}
.syntax--markup.syntax--italic {
  color: #a626a4;
  font-style: italic;
}
.syntax--markup.syntax--heading {
  color: #e45649;
}
.syntax--markup.syntax--heading .syntax--punctuation.syntax--definition.syntax--heading {
  color: #4078f2;
}
.syntax--markup.syntax--link {
  color: #0184bc;
}
.syntax--markup.syntax--inserted {
  color: #50a14f;
}
.syntax--markup.syntax--quote {
  color: #986801;
}
.syntax--markup.syntax--raw {
  color: #50a14f;
}
.syntax--source.syntax--c .syntax--keyword.syntax--operator {
  color: #a626a4;
}
.syntax--source.syntax--cpp .syntax--keyword.syntax--operator {
  color: #a626a4;
}
.syntax--source.syntax--cs .syntax--keyword.syntax--operator {
  color: #a626a4;
}
.syntax--source.syntax--css .syntax--property-name,
.syntax--source.syntax--css .syntax--property-value {
  color: #696c77;
}
.syntax--source.syntax--css .syntax--property-name.syntax--support,
.syntax--source.syntax--css .syntax--property-value.syntax--support {
  color: #383a42;
}
.syntax--source.syntax--gfm .syntax--markup {
  -webkit-font-smoothing: auto;
}
.syntax--source.syntax--gfm .syntax--link .syntax--entity {
  color: #4078f2;
}
.syntax--source.syntax--go .syntax--storage.syntax--type.syntax--string {
  color: #a626a4;
}
.syntax--source.syntax--ini .syntax--keyword.syntax--other.syntax--definition.syntax--ini {
  color: #e45649;
}
.syntax--source.syntax--java .syntax--storage.syntax--modifier.syntax--import {
  color: #c18401;
}
.syntax--source.syntax--java .syntax--storage.syntax--type {
  color: #c18401;
}
.syntax--source.syntax--java .syntax--keyword.syntax--operator.syntax--instanceof {
  color: #a626a4;
}
.syntax--source.syntax--java-properties .syntax--meta.syntax--key-pair {
  color: #e45649;
}
.syntax--source.syntax--java-properties .syntax--meta.syntax--key-pair > .syntax--punctuation {
  color: #383a42;
}
.syntax--source.syntax--js .syntax--keyword.syntax--operator {
  color: #0184bc;
}
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--delete,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--in,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--of,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--instanceof,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--new,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--typeof,
.syntax--source.syntax--js .syntax--keyword.syntax--operator.syntax--void {
  color: #a626a4;
}
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--dictionary.syntax--json > .syntax--string.syntax--quoted.syntax--json {
  color: #e45649;
}
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--dictionary.syntax--json > .syntax--string.syntax--quoted.syntax--json > .syntax--punctuation.syntax--string {
  color: #e45649;
}
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--dictionary.syntax--json > .syntax--value.syntax--json > .syntax--string.syntax--quoted.syntax--json,
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--array.syntax--json > .syntax--value.syntax--json > .syntax--string.syntax--quoted.syntax--json,
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--dictionary.syntax--json > .syntax--value.syntax--json > .syntax--string.syntax--quoted.syntax--json > .syntax--punctuation,
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--array.syntax--json > .syntax--value.syntax--json > .syntax--string.syntax--quoted.syntax--json > .syntax--punctuation {
  color: #50a14f;
}
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--dictionary.syntax--json > .syntax--constant.syntax--language.syntax--json,
.syntax--source.syntax--json .syntax--meta.syntax--structure.syntax--array.syntax--json > .syntax--constant.syntax--language.syntax--json {
  color: #0184bc;
}
.syntax--source.syntax--ruby .syntax--constant.syntax--other.syntax--symbol > .syntax--punctuation {
  color: inherit;
}
.syntax--source.syntax--python .syntax--keyword.syntax--operator.syntax--logical.syntax--python {
  color: #a626a4;
}
.syntax--source.syntax--python .syntax--variable.syntax--parameter {
  color: #986801;
}
</style>
  </head>
  <body class='markdown-preview' data-use-github-style><h1 id="docker-network-and-kubernetes-concept">Docker network and Kubernetes concept</h1>
<h2 id="1-docker-network">1. Docker network</h2>
<h3 id="docker-network-l-g-">Docker network là gì?</h3>
<p>   Docker network dùng để gắn địa chỉ IP cho các containers.</p>
<h3 id="ph-n-lo-i-docker-network">Phân loại Docker network</h3>
<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>-&nbsp;Default&nbsp;Networks</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-&nbsp;Users-defined&nbsp;Networks</span></span></span></div></pre><p><strong><em>Default Network</em></strong></p>
<p>Sau khi cài đặt Docker có 3 networks được tạo ra 1 cách tự động: brige, none, host.
Có thể kiểm tra bằng câu lệnh:</p>
<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>$docker&nbsp;network&nbsp;ls</span></span></span></div></pre><ul>
<li><p>brige là loại network mà docker sẽ tự động truy cập container tới mạng này . Bridge như một phần của host&#39;s network stack( Sử dụng câu lệnh ifconfig để kiểm tra, bridge được thể hiện bằng docker0). Muốn thay đổi network mà container chạy trên đó khi run sử dụng cờ --network:</p>
<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>$docker&nbsp;run&nbsp;--network=&lt;tennetwork&gt;</span></span></span></div></pre><p>các container có thể giao tiếp với nhau qua network này qua :</p>
<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>$docker&nbsp;run&nbsp;--link</span></span></span></div></pre></li>
<li><p>none: khi sử dụng none, container sẽ được đính kèm vào container-specific network stack.Khi mà 1 container đang chạy đính kèm vào network này thì nó có vai trò như 1 root, để xem network như thế nào trong 1 container. Container này thiếu network interface. Sử dụng câu lệnh sau để để đính kèm container vào network này:</p>
<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>$docker&nbsp;attach&nbsp;&lt;tên&gt;</span></span></span></div></pre><p> Sử dụng CTRL-p CTRL-q để detach mà container vẫn tiếp tục running.</p>
</li>
<li>host: Sử dụng network này để thêm container vào host network stack.</li>
</ul>
<p>-&gt; Sử dụng : $docker network inspect <loại network=""> để lấy thông tin về network.</loại></p>
<p><strong><em>User-defined networks</em></strong></p>
<p>Tạo những networks kiểu này nhằm mục đích quản lí các containers liên kết với nhau, hoặc cho phép phân giải một cách tự động tên miền sang địa chỉ IP.
Docker cung cấp drivers network để tạo những mạng này. Có thể tạo:</p>
<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>-bridge&nbsp;network</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>&nbsp;&nbsp;&nbsp;&nbsp;-overlay&nbsp;network</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>&nbsp;&nbsp;&nbsp;&nbsp;-MACVLAN&nbsp;network</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>&nbsp;&nbsp;&nbsp;&nbsp;-network&nbsp;plugin</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>&nbsp;&nbsp;&nbsp;&nbsp;-remote&nbsp;network</span></span></span></div></pre><ul>
<li><p>bridge network: Là lọai phổ biến nhất được sử dụng trong Docker.
Tạo network bằng câu lệnh:</p>
<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>$docker&nbsp;network&nbsp;create&nbsp;--driver&nbsp;bridge&nbsp;&lt;ten&gt;</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>&nbsp;&nbsp;$docker&nbsp;run&nbsp;--network=&lt;ten&gt;&nbsp;//cho&nbsp;phép&nbsp;container&nbsp;run&nbsp;trong&nbsp;network&nbsp;đó.</span></span></span></div></pre></li>
</ul>
<p>Loại này sẽ hữu ích cho loại network nhỏ(single host), còn đối với network lớn sẽ sử dụng overlay.</p>
<ul>
<li><p>docker-gwbridge network: Là một local bridge network.Nó sẽ được tự động được tạo ra trong hai tình huống:</p>
<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>-Khi&nbsp;tham&nbsp;gia&nbsp;một&nbsp;nhóm,&nbsp;Docker&nbsp;sử&nbsp;dụng&nbsp;network&nbsp;này&nbsp;cho&nbsp;việc&nbsp;giao&nbsp;tiếp&nbsp;giữa&nbsp;các&nbsp;node&nbsp;tại&nbsp;những&nbsp;host&nbsp;khác&nbsp;nhau.</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>&nbsp;&nbsp;-Khi&nbsp;mà&nbsp;không&nbsp;1&nbsp;network&nbsp;nào&nbsp;của&nbsp;container&nbsp;cung&nbsp;cấp&nbsp;những&nbsp;truy&nbsp;cập&nbsp;ngoài&nbsp;mạng.&nbsp;Sủ&nbsp;dụng&nbsp;network&nbsp;này&nbsp;để&nbsp;liên&nbsp;hệ&nbsp;với&nbsp;những&nbsp;network&nbsp;ngoài&nbsp;hoặc&nbsp;những&nbsp;nodes&nbsp;ở&nbsp;nhóm&nbsp;khác.</span></span></span></div></pre><p>Nó luôn luôn xuất hiện khi sử dụng network overlay.</p>
</li>
<li>overlay networks in swarm mode: network này sẽ có trên những nodes trong swarm mà không cần tới external key-value.</li>
<li>overlay networks without swarm mode: Nếu không ở chế độ swarm mode thì overlay network yêu cầu phải có một key-value store service.</li>
</ul>
<p><img src="http://i.imgur.com/06lXPbP.png" alt="anh1"></p>
<p>Mỗi host trong network phải run một Docker Engine instance. Cách dễ dàng nhất để tạo ra các host là sử dụng Docker Machine.</p>
<ul>
<li>custom network plugins: Sử dụng plugin của Docker để viết lên những network driver plugin. Nó sẽ chạy như 1 tiến trình tách biệt trên máy chủ. Những plugin này sẽ có những quy tắc, vòng đời: cài đặt, bắt đầu, hoạt động, dừng.<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span>&nbsp;&nbsp;</span><span class="syntax--meta syntax--paragraph syntax--text"><span>$&nbsp;docker&nbsp;network&nbsp;create&nbsp;--driver&nbsp;weave&nbsp;mynet</span></span></span></div></pre></li>
<li>Embedded DNS server: Cung cấp hoạt động phân giải tên miền giữa các containers.</li>
</ul>
<h2 id="2-calico-flannel-weave">2. Calico, Flannel, Weave</h2>
<p>Có 4 giải pháp khác nhau cho 1 network với nhiều hosts: Calico, Flannel, Weave, Docker Overlay Network.</p>
<p>Trong đó:</p>
<pre class="editor-colors lang-text"><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>-&nbsp;Calico:&nbsp;1&nbsp;giải&nbsp;pháp&nbsp;cho&nbsp;network&nbsp;nhiều&nbsp;host.</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>-&nbsp;Flannel:&nbsp;dành&nbsp;cho&nbsp;overlay&nbsp;network.</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>-&nbsp;Weave:&nbsp;quản&nbsp;lí&nbsp;network</span></span></span></div><div class="line"><span class="syntax--text syntax--plain"><span class="syntax--meta syntax--paragraph syntax--text"><span>-&nbsp;Docker&nbsp;Overlay&nbsp;Network:&nbsp;giải&nbsp;pháp&nbsp;cho&nbsp;overlay&nbsp;network&nbsp;với&nbsp;ectd.</span></span></span></div></pre><h2 id="3-kubernetes">3. Kubernetes</h2>
<h3 id="kubernetes-">Kubernetes?</h3>
<p>Kubernetes là 1 project opensource được phát triển bởi Google. Kubernetes phục vụ cho việc deploy, scale và operator các application container trên các cụm máy chủ dùng container app làm trung tâm.</p>
<p>Với Kubernetes:</p>
<ul>
<li>Deploy app một cách nhanh nhất.</li>
<li>Hỗ trợ tự động scale app.</li>
<li>Liên tục tích hợp các tính năng mới.</li>
<li>Tối ưu hóa phần cứng (cho phép người dùng lựa chọn resource mà người đó cần).</li>
</ul>
<h3 id="kubernetes-components-">Kubernetes components:</h3>
<p>Dưới đây là hình ảnh về các thành phần trong Kubernetes:</p>
<p><img src="http://sv1.upsieutoc.com/2017/05/13/Screenshotfrom2017-05-1309-56-27.png" alt="anh2"></p>
<p>Trong đó:</p>
<ul>
<li>Pod: tập hợp các container lại, các container đã được schedule.</li>
<li>Kuberlet: Khởi động, duy trì pod.</li>
<li>Label: dạng key-value, định nghĩa đơn giản nhiệm vụ của các Pod.</li>
<li>Proxy: cơ chế truy cập tới node.</li>
<li>Master: nhận những thay đổi về cài đặt và triển khai.</li>
<li>API server: cung cấp Kubernetes API. Đặt Pod vào node, đồng bộ hóa thông tin của Pod bằng REST API.</li>
<li>etcd: liên kết cài đặt với node.</li>
</ul>
<h2 id="end-">end.</h2></body>
</html>
