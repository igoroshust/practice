/* Здесь содержится оптимальный (с точки зрения ИИ) код оформления показа модалок */

const modalButtons = document.querySelectorAll('[data-modal-button]');
const modalCloseButtons = document.querySelectorAll('[data-modal-close]');

// Единый обработчик для всех модальных окон
function setupModalHandlers() {
    // Обработчик клика по документу (делегирование)
    document.addEventListener('click', function(event) {
        const target = event.target;

        // 1. Открытие модального окна по кнопке
        if (target.matches('[data-modal-button]')) {
            const modalId = target.dataset.modalButton;
            const modal = document.getElementById(modalId);
            
            if (modal) {
                modal.classList.remove('content-hidden');
            }
            return; // Прерываем, чтобы не обрабатывать дальше
        }

        // 2. Закрытие по кнопке закрытия
        if (target.matches('[data-modal-close]')) {
            const modal = target.closest('[data-modal]');
            
            if (modal) {
                modal.classList.add('content-hidden');
            }
            return;
        }

        // 3. Блокировка закрытия при клике внутри .modal-window
        if (target.closest('.modal-window')) {
            event.stopPropagation();
            return;
        }

        // 4. Закрытие при клике на бэкграунд (сам элемент [data-modal])
        if (target.matches('[data-modal]')) {
            target.classList.add('content-hidden');
        }
    });
}

// Инициализация
setupModalHandlers();
