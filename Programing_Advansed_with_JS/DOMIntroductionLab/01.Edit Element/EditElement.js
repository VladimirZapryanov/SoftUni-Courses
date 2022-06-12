function editElement(arg1, arg2, arg3) {
   let text = arg1.textContent;
   let match = arg2;
   let replacer = arg3;

   let pattern = new RegExp(match, 'g');
   let result = text.replace(pattern, replacer);

   arg1.textContent = result;
}

