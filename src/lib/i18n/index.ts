import i18next from 'i18next';
import resourcesToBackend from 'i18next-resources-to-backend';
import LanguageDetector from 'i18next-browser-languagedetector';
import type { i18n as i18nType } from 'i18next';
import { writable } from 'svelte/store';

const createI18nStore = (i18n: i18nType) => {
	const i18nWritable = writable(i18n);

	i18n.on('initialized', () => {
		i18nWritable.set(i18n);
	});
	i18n.on('loaded', () => {
		i18nWritable.set(i18n);
	});
	i18n.on('added', () => i18nWritable.set(i18n));
	i18n.on('languageChanged', () => {
		i18nWritable.set(i18n);
	});
	return i18nWritable;
};

const createIsLoadingStore = (i18n: i18nType) => {
	const isLoading = writable(false);

	// if loaded resources are empty || {}, set loading to true
	i18n.on('loaded', (resources) => {
		// console.log('loaded:', resources);
		isLoading.set(Object.keys(resources).length === 0);
	});

	// if resources failed loading, set loading to true
	i18n.on('failedLoading', () => {
		isLoading.set(true);
	});

	return isLoading;
};

export const normalizeLang = (language?: string) => {
	if (!language) return 'sq-AL';
	if (language === 'sq' || language.startsWith('sq-') || language.startsWith('al')) {
		return 'sq-AL';
	}
	return language;
};

export const initI18n = (defaultLocale?: string | undefined) => {
	const targetLocale = normalizeLang(defaultLocale || 'sq-AL');
	const detectionOrder = ['querystring', 'localStorage'];
	const fallbackDefaultLocale = [targetLocale, 'sq-AL'];

	const loadResource = (language: string, namespace: string) => {
		const lang = normalizeLang(language);
		return import(`./locales/${lang}/${namespace}.json`);
	};

	i18next
		.use(resourcesToBackend(loadResource))
		.use(LanguageDetector)
		.init({
			debug: false,
			lng: targetLocale,
			detection: {
				order: detectionOrder,
				caches: ['localStorage'],
				lookupQuerystring: 'lang',
				lookupLocalStorage: 'locale'
			},
			fallbackLng: {
				sq: ['sq-AL'],
				'sq-AL': ['sq-AL'],
				'sq-XK': ['sq-AL'],
				'al-AL': ['sq-AL'],
				default: fallbackDefaultLocale
			},
			ns: 'translation',
			returnEmptyString: false,
			interpolation: {
				escapeValue: false // nuk nevojitet për svelte pasi i bën escape vetë
			}
		});

	const lang = normalizeLang(i18next?.language) || targetLocale;
	if (typeof document !== 'undefined') {
		document.documentElement.setAttribute('lang', lang);
	}
};

const i18n = createI18nStore(i18next);
const isLoadingStore = createIsLoadingStore(i18next);

export const getLanguages = async () => {
	const languages = (await import(`./locales/languages.json`)).default;
	return languages;
};
export const changeLanguage = (lang: string) => {
	const target = normalizeLang(lang);
	if (typeof document !== 'undefined') {
		document.documentElement.setAttribute('lang', target);
	}
	if (typeof localStorage !== 'undefined') {
		localStorage.locale = target;
	}
	i18next.changeLanguage(target);
};

export default i18n;
export const isLoading = isLoadingStore;
