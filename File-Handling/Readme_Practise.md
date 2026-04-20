🧠 Important Points
✔ File close करना जरूरी (या with use करो)
✔ "w" → data delete कर देता है
✔ "a" → safe add करता है

🟢 1. File Handling क्या है?

👉 File में data read / write / append करना
👉 Example: .txt, .csv, logs

🟡 2. File Open Syntax
file = open("file_name", "mode")

🔵 3. Modes (बहुत Important 🔥)
Mode	काम
"r"	Read (error अगर file ना हो)
"w"	Write (पुराना data delete)
"a"	Append (data add)
"x"	Create new file (error अगर already exist)

🟣 4. File Read Methods
file.read()        # पूरा file
file.readline()    # एक line
file.readlines()   # list of lines