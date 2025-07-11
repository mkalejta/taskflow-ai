import { TaskStatus } from '../types/enums';

export const SECTION_TITLES = {
    [TaskStatus.TODO]: 'All Tasks',
    [TaskStatus.IN_PROGRESS]: 'In Progress',
    [TaskStatus.DONE]: 'Completed'
} as const;

export const BUTTON_VARIANTS = {
    DEFAULT: 'default',
    NAV: 'nav',
    SIDEBAR: 'sidebar'
} as const;