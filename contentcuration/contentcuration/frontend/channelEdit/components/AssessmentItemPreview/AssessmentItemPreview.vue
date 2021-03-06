<template>

  <div>
    <VLayout align-top justify-space-between>
      <VFlex mt-2>
        <div class="caption grey--text mb-2">
          {{ kindLabel }}
        </div>
        <MarkdownViewer :markdown="question" />
      </VFlex>
    </VLayout>

    <VLayout
      v-if="detailed && !isPerseus"
      mt-3
      data-test="item-answers-preview"
    >
      <VFlex>
        <div class="caption grey--text mb-2">
          {{ $tr('answersLabel') }}
        </div>

        <div v-if="!answers || !answers.length">
          {{ $tr('noAnswersPlaceholder') }}
        </div>

        <template v-else>
          <template v-if="isSingleSelection || isTrueFalse">
            <VRadioGroup v-model="correctAnswersIndices">
              <VRadio
                v-for="(answer, idx) in answers"
                :key="idx"
                :value="idx"
                readonly
              >
                <template #label>
                  <div class="px-2">
                    <MarkdownViewer :markdown="answer.answer" />
                  </div>
                </template>
              </VRadio>
            </VRadioGroup>
          </template>

          <template v-if="isMultipleSelection">
            <Checkbox
              v-for="(answer, idx) in answers"
              :key="idx"
              v-model="correctAnswersIndices"
              :value="idx"
              readonly
            >
              <template #label>
                <div class="px-2">
                  <MarkdownViewer :markdown="answer.answer" />
                </div>
              </template>
            </Checkbox>
          </template>

          <VList v-if="isInputQuestion">
            <VListTile
              v-for="(answer, idx) in answers"
              :key="idx"
            >
              {{ answer.answer }}
            </VListTile>
          </VList>
        </template>

        <div class="mt-1">
          <!--
            class="hints-preview" is needed for precise click
            target detection in AssessmentView.vue
          -->
          <span v-if="hintsCount === 0">{{ $tr('noHintsPlaceholder') }}</span>
          <div v-else class="hints-preview">
            <span
              class="hints-toggle"
              data-test="hintsToggle"
              @click="areHintsOpen= !areHintsOpen"
            >
              <span>{{ hintsToggleLabel }}</span>

              <span class="icon">
                <Icon v-if="areHintsOpen" small>arrow_drop_down</Icon>
                <Icon v-else small>arrow_drop_up</Icon>
              </span>
            </span>

            <VList v-if="areHintsOpen">
              <VListTile
                v-for="(hint, hintIdx) in hints"
                :key="hintIdx"
              >
                <VFlex xs1>
                  {{ hintIdx + 1 }}
                </VFlex>
                <VFlex class="px-2">
                  <MarkdownViewer :markdown="hint.hint" />
                </VFlex>
              </VListTile>
            </VList>
          </div>
        </div>
      </VFlex>
    </VLayout>
  </div>

</template>

<script>

  import sortBy from 'lodash/sortBy';
  import { AssessmentItemTypes, AssessmentItemTypeLabels } from '../../constants';
  import { getCorrectAnswersIndices } from '../../utils';
  import translator from '../../translator';

  import Checkbox from 'shared/views/form/Checkbox';
  import MarkdownViewer from 'shared/views/MarkdownEditor/MarkdownViewer/MarkdownViewer.vue';

  export default {
    name: 'AssessmentItemPreview',
    components: {
      MarkdownViewer,
      Checkbox,
    },
    props: {
      /**
       * An assessment item as retrieved from API:
       * {
       *    question
       *    type
       *    order
       *    answers
       *    hints
       *    ...
       * }
       */
      item: {
        type: Object,
      },
      detailed: {
        type: Boolean,
        default: false,
      },
    },
    data() {
      return {
        areHintsOpen: false,
      };
    },
    computed: {
      question() {
        if (!this.item || !this.item.question) {
          return '';
        }

        return this.item.question;
      },
      kind() {
        if (!this.item || !this.item.type) {
          return '';
        }

        return this.item.type;
      },
      isPerseus() {
        return this.kind === AssessmentItemTypes.PERSEUS_QUESTION;
      },
      answers() {
        if (!this.item || !this.item.answers) {
          return [];
        }

        return sortBy(this.item.answers, 'order');
      },
      hints() {
        if (!this.item || !this.item.hints) {
          return [];
        }

        return sortBy(this.item.hints, 'order');
      },
      kindLabel() {
        return translator.$tr(AssessmentItemTypeLabels[this.kind]);
      },
      isSingleSelection() {
        return this.kind === AssessmentItemTypes.SINGLE_SELECTION;
      },
      isMultipleSelection() {
        return this.kind === AssessmentItemTypes.MULTIPLE_SELECTION;
      },
      isTrueFalse() {
        return this.kind === AssessmentItemTypes.TRUE_FALSE;
      },
      isInputQuestion() {
        return this.kind === AssessmentItemTypes.INPUT_QUESTION;
      },
      correctAnswersIndices() {
        return getCorrectAnswersIndices(this.kind, this.answers);
      },
      hintsToggleLabel() {
        if (this.areHintsOpen) {
          return this.$tr('hintsToggleLabelHide');
        }

        return this.$tr('hintsToggleLabelShow', { hintsCount: this.hintsCount });
      },
      hintsCount() {
        if (!this.hints) {
          return 0;
        }

        return this.hints.length;
      },
    },
    $trs: {
      answersLabel: 'Answers',
      noAnswersPlaceholder: 'Question has no answer options',
      noHintsPlaceholder: 'Question has no hints',
      hintsToggleLabelHide: 'Hide hints',
      hintsToggleLabelShow: 'Show {hintsCount} {hintsCount, plural, one {hint} other {hints}}',
    },
  };

</script>

<style lang="less" scoped>

  .hints-toggle {
    text-decoration: underline;
    cursor: pointer;

    .icon {
      position: relative;
      top: -4px;
    }
  }

  /deep/ .v-input--selection-controls {
    margin-top: 0;

    .accent--text {
      color: gray !important;
    }

    .v-input__slot {
      margin-bottom: 0 !important;
    }
  }

  /deep/ img {
    max-width: 100%;
    height: auto;
  }

</style>
