from enum import Enum


class MESSAGES(str, Enum):
    DEFAULT = lambda msg="": f"{msg if msg else ''}"
    MODEL_ADDED = lambda model="": f"Modeli '{model}' u shtua me sukses."
    MODEL_DELETED = (
        lambda model="": f"Modeli '{model}' u fshi me sukses."
    )


class WEBHOOK_MESSAGES(str, Enum):
    DEFAULT = lambda msg="": f"{msg if msg else ''}"
    USER_SIGNUP = lambda username="": (
        f"Përdorues i ri u regjistrua: {username}" if username else "Përdorues i ri u regjistrua"
    )


class ERROR_MESSAGES(str, Enum):
    def __str__(self) -> str:
        return super().__str__()

    DEFAULT = (
        lambda err="": f'{"Diçka shkoi keq :/" if err == "" else "[GABIM: " + str(err) + "]"}'
    )
    ENV_VAR_NOT_FOUND = "Variabla e nevojshme e mjedisit nuk u gjet. Po ndërpritet ekzekutimi."
    CREATE_USER_ERROR = "Ups! Diçka shkoi keq gjatë krijimit të llogarisë suaj. Ju lutem provoni përsëri më vonë. Nëse problemi vazhdon, kontaktoni mbështetjen teknike."
    DELETE_USER_ERROR = "Ups! Diçka shkoi keq gjatë fshirjes së përdoruesit. Ju lutem provoni përsëri."
    EMAIL_MISMATCH = "Kjo adresë email nuk përputhet me emailin e regjistruar tek ofruesi juaj. Ju lutem kontrolloni emailin dhe provoni përsëri."
    EMAIL_TAKEN = "Ky email është i regjistruar tashmë. Identifikohuni me llogarinë ekzistuese ose përdorni një email tjetër."
    USERNAME_TAKEN = (
        "Ky emër përdoruesi është i regjistruar tashmë. Ju lutem zgjidhni një emër tjetër."
    )
    PASSWORD_TOO_LONG = "Fjalëkalimi që keni vendosur është shumë i gjatë. Sigurohuni që fjalëkalimi të jetë më pak se 72 bajt."
    COMMAND_TAKEN = "Kjo komandë është e regjistruar tashmë. Ju lutem zgjidhni një komandë tjetër."
    FILE_EXISTS = "Ky skedar është i regjistruar tashmë. Ju lutem zgjidhni një skedar tjetër."

    ID_TAKEN = "Kjo ID është e regjistruar tashmë. Ju lutem zgjidhni një ID tjetër."
    MODEL_ID_TAKEN = "Kjo ID e modelit është e regjistruar tashmë. Ju lutem zgjidhni një ID tjetër."
    NAME_TAG_TAKEN = "Kjo etiketë emri është e regjistruar tashmë. Ju lutem zgjidhni një tjetër."
    MODEL_ID_TOO_LONG = "ID e modelit është shumë e gjatë. Sigurohuni që të jetë më pak se 256 karaktere."

    INVALID_TOKEN = (
        "Sesioni juaj ka skaduar ose token-i është i pavlefshëm. Ju lutem identifikohuni përsëri."
    )
    INVALID_CRED = "Emaili ose fjalëkalimi i dhënë është i pasaktë. Ju lutem kontrolloni të dhënat dhe provoni përsëri."
    INVALID_EMAIL_FORMAT = "Formati i emailit është i pavlefshëm. Ju lutem vendosni një adresë të vlefshme emaili (p.sh., emri@shembull.al)."
    INCORRECT_PASSWORD = (
        "Fjalëkalimi i vendosur është i pasaktë. Ju lutem kontrolloni dhe provoni përsëri."
    )
    INVALID_TRUSTED_HEADER = "Ofruesi juaj nuk ka dhënë një krye (header) të besuar. Kontaktoni administratorin tuaj për ndihmë."

    EXISTING_USERS = "Nuk mund të çaktivizoni autentikimin sepse ka përdorues ekzistues në sistem."

    UNAUTHORIZED = "401 I paautorizuar"
    ACCESS_PROHIBITED = "Nuk keni leje për të hyrë në këtë burim. Ju lutem kontaktoni administratorin tuaj."
    ACTION_PROHIBITED = (
        "Veprimi i kërkuar është kufizuar për arsye sigurie."
    )

    FILE_NOT_SENT = "FILE_NOT_SENT"
    FILE_NOT_SUPPORTED = "Ups! Formati i këtij skedari nuk mbështetet. Ju lutem ngarkoni një skedar me format të mbështetur dhe provoni përsëri."

    NOT_FOUND = "Nuk mundëm të gjejmë atë që po kërkoni :/"
    USER_NOT_FOUND = "Përdoruesi nuk u gjet :/"
    API_KEY_NOT_FOUND = "Ups! Çelësi API mungon. Ju lutem vendosni një çelës të vlefshëm API për të përdorur këtë funksion."
    API_KEY_NOT_ALLOWED = "Përdorimi i çelësave API nuk është i aktivizuar në këtë mjedis."

    MALICIOUS = "U zbuluan aktivitete të pazakonta, ju lutem provoni përsëri pas disa minutash."

    PANDOC_NOT_INSTALLED = "Pandoc nuk është i instaluar në server. Ju lutem kontaktoni administratorin tuaj."
    INCORRECT_FORMAT = (
        lambda err="": f"Format i pavlefshëm. Ju lutem përdorni formatin e saktë{err}"
    )
    RATE_LIMIT_EXCEEDED = "U tejkalua kufiri i kërkesave në API"

    MODEL_NOT_FOUND = lambda name="": f"Modeli '{name}' nuk u gjet"
    OPENAI_NOT_FOUND = lambda name="": "API e OpenAI nuk u gjet"
    OLLAMA_NOT_FOUND = "Ndërfaqja nuk mund të lidhet me Ollama"
    CREATE_API_KEY_ERROR = "Ups! Diçka shkoi keq gjatë krijimit të çelësit API. Ju lutem provoni përsëri më vonë."
    API_KEY_CREATION_NOT_ALLOWED = "Krijimi i çelësave API nuk lejohet në këtë mjedis."

    EMPTY_CONTENT = "Përmbajtja e dhënë është bosh. Sigurohuni që të keni vendosur tekst ose të dhëna para se të vazhdoni."

    DB_NOT_SQLITE = "Ky funksion është i disponueshëm vetëm kur përdoret baza e të dhënave SQLite."

    INVALID_URL = (
        "Ups! URL-ja e dhënë është e pavlefshme. Ju lutem kontrolloni dhe provoni përsëri."
    )

    WEB_SEARCH_ERROR = (
        lambda err="": f"{err if err else 'Ups! Diçka shkoi keq gjatë kërkimit në ueb.'}"
    )

    OLLAMA_API_DISABLED = (
        "API e Ollama është e çaktivizuar. Ju lutem aktivizojeni për të përdorur këtë funksion."
    )

    FILE_TOO_LARGE = (
        lambda size="": f"Ups! Skedari që po ngarkoni është shumë i madh. Ju lutem ngarkoni një skedar më të vogël se {size}."
    )

    DUPLICATE_CONTENT = (
        "U zbulua përmbajtje e dyfishuar. Ju lutem jepni përmbajtje unike për të vazhduar."
    )
    FILE_NOT_PROCESSED = "Përmbajtja e nxjerrë nuk është e disponueshme për këtë skedar. Ju lutem sigurohuni që skedari të jetë përpunuar para se të vazhdoni."

    INVALID_PASSWORD = lambda err="": (
        err if err else "Fjalëkalimi nuk i plotëson kriteret e kërkuara të sigurisë."
    )


class TASKS(str, Enum):
    def __str__(self) -> str:
        return super().__str__()

    DEFAULT = lambda task="": f"{task if task else 'generation'}"
    TITLE_GENERATION = "title_generation"
    FOLLOW_UP_GENERATION = "follow_up_generation"
    TAGS_GENERATION = "tags_generation"
    EMOJI_GENERATION = "emoji_generation"
    QUERY_GENERATION = "query_generation"
    IMAGE_PROMPT_GENERATION = "image_prompt_generation"
    AUTOCOMPLETE_GENERATION = "autocomplete_generation"
    FUNCTION_CALLING = "function_calling"
    MOA_RESPONSE_GENERATION = "moa_response_generation"
