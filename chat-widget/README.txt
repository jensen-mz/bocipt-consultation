BOCI-Prudential chat widget mockup
==================================

HOW TO OPEN
  Double-click index.html. No build step, no internet, no server needed.

FILES
  index.html   the widget (all HTML + JS)
  style.css    the widget's styles
  README.txt   this file

ADDING THE CLIENT WEBSITE SCREENSHOT
  Put your screenshot of the BOCIPT website in this same folder
  (the one holding index.html) and name it exactly:

      site.png

  That is the whole setup. Reload index.html and the screenshot fills the
  background behind the chat widget automatically. Nothing else to edit.

  Recommended size: 1440 x 900 pixels (a normal desktop browser window).
  It is scaled to cover the window, so anything wider or taller also works.
  If you would rather use a JPG, name it site.jpg and change the single
  line  const SITE_BG = 'site.png';  in index.html to  'site.jpg'.

  If site.png is not there, the page shows a dashed placeholder box instead.
  That is intentional and harmless - the widget still works exactly the same.

ADDING YOUR OWN LAUNCHER ICON
  Put a square PNG in this same folder and name it exactly:

      icon.png

  Reload index.html and it replaces the white speech-bubble in the red
  bottom-right button. The red circle stays behind it, so a transparent
  logo works too. Any square size is fine - it is scaled to fill the button.

  If icon.png is not there, the original speech-bubble icon is used.
  Nothing breaks either way.

ABOUT THE DEMO
  Three languages: EN / 繁 / 简. Seven hard-coded response types:
  text with citations, image with chart, internal document (no citation),
  routing to eMPF, refusal / guardrail, account card, escalation to a human.
  All answers are pre-written. There is no live model and no live data.
  Click the red bubble bottom-right, accept the disclaimer, then either type
  a question or use one of the suggested chips.

THE CONSENT SWITCHER (for the workshop)
  There is a small dark box in the top-left corner. It is a demo control,
  not part of the product, and it switches which consent screen the widget
  shows. Pick one, then open the chat as normal. Only one is on at a time.

      A  Modal         the notice as a pop-up card over the chat, with a
                       warning icon and two buttons. Hard to miss.
      B  Chat message  the notice arrives as the assistant's first message,
                       with the agree button inside the bubble. After you
                       agree, your consent is kept as your own message
                       ("I consent to…"), and the assistant greets you next.
                       A, the pop-up, does not leave that line: the greeting
                       is the first message. C does the same as B.
      C  Full terms    a long terms document that opens to the LEFT of the
                       widget. The confirm button stays greyed out until you
                       have scrolled all the way to the bottom. On a narrow
                       screen there is no room beside the widget, so the same
                       terms open inside the chat panel instead.

  Until the notice is accepted, the typing box and send button are greyed out
  with a short line explaining why. This is the same for all three, so the
  choice is about the layout, not about whether input is locked.

  The wording in C is PLACEHOLDER text, written for this demo and marked as
  such on screen. Compliance must replace it before anything goes live. It
  deliberately cites no regulatory clause numbers.

  Nothing is remembered between sessions - reloading the page starts again
  at A with the notice unaccepted.
