<template>

  <VList
    v-if="items && items.length"
    two-line
  >
    <template v-for="(item, itemIdx) in items">
      <VListTile
        :key="`list-tile-${itemIdx}`"
        data-test="resource"
      >
        <VListTileAction>
          <ContentNodeIcon
            v-if="item.kind"
            :kind="item.kind"
            :size="20"
          />
        </VListTileAction>

        <VListTileContent>
          <VListTileTitle>
            <ActionLink
              class="notranslate"
              data-test="resourceLink"
              @click="onItemClick(item.id)"
            >
              {{ item.title }}
            </ActionLink>
          </VListTileTitle>
          <VListTileSubTitle class="notranslate">
            {{ item.parentTitle }}
          </VListTileSubTitle>
        </VListTileContent>

        <VListTileAction>
          <VTooltip bottom>
            <template slot="activator" slot-scope="{ on }">
              <VBtn
                icon
                data-test="resourceRemoveBtn"
                v-on="on"
                @click="onRemoveClick(item.id)"
              >
                <Icon>clear</Icon>
              </VBtn>
            </template>
            <span>{{ removeBtnLabel }}</span>
          </VTooltip>
        </VListTileAction>
      </VListTile>

      <VDivider :key="`divider-${itemIdx}`" />
    </template>
  </VList>

</template>

<script>

  import ActionLink from 'shared/views/ActionLink';
  import ContentNodeIcon from 'shared/views/ContentNodeIcon';
  import Icon from 'shared/views/Icon';

  export default {
    name: 'RelatedResourcesList',
    components: {
      ActionLink,
      ContentNodeIcon,
      Icon,
    },
    props: {
      /**
       * An array of node items satisfying
       * following interface:
       * {
       *   id: ...,
       *   title: ...,
       *   kind: ...,
       *   parentTitle: ...
       * }
       */
      items: {
        type: Array,
        required: true,
      },
      removeResourceBtnLabel: {
        type: String,
        required: false,
      },
    },
    computed: {
      removeBtnLabel() {
        return this.removeResourceBtnLabel || this.$tr('removeBtnLabel');
      },
    },
    methods: {
      onRemoveClick(id) {
        this.$emit('removeItemClick', id);
      },
      onItemClick(id) {
        this.$emit('itemClick', id);
      },
    },
    $trs: {
      removeBtnLabel: 'Remove',
    },
  };

</script>
