export function blockPasteOverLimit(event, maxLength = 8) {
  const input = event.target;
  const pastedText = event.clipboardData?.getData("text") ?? "";
  const selectionLength = (input.selectionEnd ?? 0) - (input.selectionStart ?? 0);
  const resultingLength = input.value.length - selectionLength + pastedText.length;

  if (resultingLength > maxLength) {
    event.preventDefault();
  }
}
